#!/usr/bin/env python3
import sys
import os
import numpy as np
import datetime
import time
import yaml

from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5 import QtGui, QtCore

from package.chamber import PressureChamber
from package.ui	import mainwindow


class VestController(QMainWindow, mainwindow.Ui_MainWindow):

	signal_stop_plot = QtCore.pyqtSignal()
	signal_stop_idle = QtCore.pyqtSignal()
	signal_stop_run = QtCore.pyqtSignal()

	def __init__(self, chamber_info, plot=False, debug_gui=False, tune=False):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.setWindowTitle("Pressure Vest Controller")

		# system attributes
		self.run_on = False
		self.t_app_start = time.time()

		# timing attributes
		with open('system_params.yaml') as f: 
			self.system_params = yaml.load(f, Loader=yaml.FullLoader)

		

		# self.system_params['freq']['sense'] = 5 # (Hz) TODO: set value, make external
		# self.system_params['freq']['display'] = 1 # (Hz) TODO: set value, make external
		# self.system_params['freq']['control'] = 1 # (Hz) TODO: set value, make external
		# self.system_params['freq']['log'] = 1 # (Hz) TODO: set value, make external
		# self.system_params['freq']['pwm'] = 45 # (Hz) TODO: set value, make external

		# system signals & slots
		self.pushButton_on.clicked.connect(lambda: self.switchSystemState())

		# configure ADC, GPIO, and PWM
		self.debug_gui = debug_gui
		if not debug_gui:
			from package import adc
			last_channel = 7 #TODO: set last_channel
			self.adc = adc.Adc(0, 0, last_channel) 
			
			import RPi.GPIO as GPIO
			self.GPIO = GPIO
			self.GPIO.setmode(self.GPIO.BCM)
			self.pin_pump1 = 6
			self.pin_pump2 = 5
			self.GPIO.setup(self.pin_pump1, self.GPIO.OUT)
			self.GPIO.setup(self.pin_pump2, self.GPIO.OUT)
			self.GPIO.output(self.pin_pump1, self.GPIO.LOW)
			self.GPIO.output(self.pin_pump2, self.GPIO.LOW)

			# instantiate PWM
			# from package.pca9685_driver import Device
			# self.pwm = Device(0x40) # instantiate PCA9685 #TODO: uncomment
			# self.pwm.set_pwm_frequency(self.system_params['freq']['pwm']) # (Hz)
			#TODO: ensure that initial PWM duties are 0

		# instantiate chambers
		# ~ self.chamber_info = chamber_info
		self.n_chambers = len(chamber_info)
		self.pressures = [0]*self.n_chambers # chamber pressures
		self.chambers = chamber_info # dict of chambers
		for key, chamber in self.chambers.items():
			chamber['obj'] = PressureChamber(self, key) # instantiate PressureChamber for each chamber
	
		# set up sensor idle thread
		self.thread_idle = IdleThread(self.system_params['freq']['sense'], 
			self.system_params['freq']['display']) # instantiate thread object
		self.signal_stop_idle.connect(self.thread_idle.stop) # set up signal to stop thread
		self.thread_idle.signal_sense.connect(self.sensorUpdate) # connect sensor update signal
		self.thread_idle.signal_display.connect(self.sensorDisplayUpdate) # connect display update signal
		self.thread_idle.start() # start thread

		# set up control/log run thread		
		self.thread_run = RunThread(self.system_params['freq']['control'], 
			self.system_params['freq']['display'], self.system_params['freq']['log'])
		self.signal_stop_run.connect(self.thread_run.stop) # set up signal to stop thread
		self.thread_run.signal_control.connect(self.controlUpdate)
		self.thread_run.signal_display.connect(self.systemDisplayUpdate)
		self.thread_run.signal_log.connect(self.logUpdate)

		# set up plot window if plotting on
		self.plot = plot
		if plot:
			from package import plotter
			self.plot_freq = 2 # (Hz) TODO
			plot_window = 6 # (s)
			buffer_len = round(plot_window*self.plot_freq)
			self.plot_window = plotter.PlotWindow(self.chambers, buffer_len, 
				self.signal_stop_plot)

			action_plot = QtGui.QAction('Plot data', self)
			action_plot.setShortcut("Ctrl+P")
			action_plot.setStatusTip('Plot chamber pressure data')
			action_plot.triggered.connect(self.showPlotter)
			self.menu_file = self.menuBar.addMenu('&File')
			self.menu_file.addAction(action_plot)

		# set up control tuning window if on
		self.tune = tune
		if tune:
			from package import tuner
			self.tune_window = tuner.TuneWindow(self)
			# self.tune_window.show()

			action_tune = QAction('Tune controller', self)
			action_tune.setShortcut("Ctrl+T")
			action_tune.setStatusTip('Tune pressure controller parameters')
			action_tune.triggered.connect(self.tune_window.show)
			self.menu_file = self.menuBar.addMenu('&File')
			self.menu_file.addAction(action_tune)


		#TODO: put somewhere
		# pixmap = QtGui.QPixmap('designer/img/ant.jpg')
		self.label_2.setPixmap(QtGui.QPixmap("designer/img/anterior.png"))
		self.label_2.setScaledContents(True)


	def showPlotter(self):
		self.plot_window.show()
		self.thread_plot = PlotThread(self.plot_window, self.plot_freq)
		self.signal_stop_plot.connect(self.thread_plot.stop) # set up signal to stop thread
		self.thread_plot.signal_plot.connect(self.plot_window.updateDisplay)
		self.thread_plot.start()


	def switchSystemState(self):
		if self.run_on is False:
			self.run()
		else: # self.run_on is True
			self.stop()


	def run(self):
		self.run_on = True
		self.GPIO.output(self.pin_pump1, self.GPIO.HIGH) #DEBUG
		self.GPIO.output(self.pin_pump2, self.GPIO.HIGH) #DEBUG
		self.pushButton_on.setText('Stop')
		self.pushButton_on.setStyleSheet("background-color: rgb(235, 64, 52);\n")
		print('running...') #DEBUG
		self.initLog() # initialize data log
		self.thread_run.start()


	def stop(self):
		self.run_on = False
		self.GPIO.output(self.pin_pump1, self.GPIO.LOW) #DEBUG
		self.GPIO.output(self.pin_pump2, self.GPIO.LOW) #DEBUG
		self.pushButton_on.setText('Run')
		self.pushButton_on.setStyleSheet("background-color: rgb(0, 170, 0);\n")
		print('stopped!') #DEBUG
		self.signal_stop_run.emit() # emit run stop signal
		self.controlUpdate(vent=True) # turn off all
		# print(self.data[0:10,:]) #DEBUG
		self.saveLog()
		

	def initLog(self):
		# Initialize data array for logging pressure data
		max_samples = round(self.system_params['freq']['log']*60*60) # allocate 1 hour
		self.data = np.zeros((max_samples,self.n_chambers+1), dtype=float) # allocate data array 
		self.n_samples = 0 # initialize number of data samples recorded
		self.datetime_start = datetime.datetime.now() # get start date & time


	def sensorUpdate(self, t):
		# Read/convert pressures from ADC & update pressure of each chamber object
		if not self.debug_gui:
			data = self.adc.readAll() # read pressures #TODO: uncomment
			# ~ print(data)
		else: # for debugging
			data = []
			for idx in range(0,self.n_chambers+1):
				counts = np.sin(t + idx*0.25*np.pi)*1000 # + 2047
				data.append([idx,counts])
			# pressures = np.sin(t + np.array([0,0.25,0.5,0.75])*np.pi) + 2.5 #DEBUG

		for chamber in self.chambers.values(): # update chamber pressures
			idx_adc = chamber['adc'] # ADC index of pressure chamber
			counts = data[idx_adc][1] # corresponding pressure data point
			Vs = 5.0
			pressure = (counts*(5.0/4095.0) - 0.10*Vs)*(5.0/(0.8*Vs)) # transfer function
			
			chamber['obj'].updateMeasurement(pressure) # update chamber measurement
			self.pressures[idx_adc] = pressure # update pressures in class (in order of ADC)
			
			# ~ idx_adc = self.chamber_info[name]['adc'] # ADC index of pressure chamber
			# ~ chamber.updateMeasurement(pressures[idx_adc]) # update chamber measurement
			# ~ self.pressures[idx_adc] = pressures[idx_adc] # update pressures in class (in order of ADC)


	def sensorDisplayUpdate(self,t):
		for chamber in self.chambers.values(): # update chamber pressures
			chamber['obj'].updateMeasurementDisplay()


	def controlUpdate(self, t=None, vent=False):
		if not vent: # if vent is False
			dutys = [0]*self.n_chambers 
			for chamber in self.chambers.values(): # calculate duty cycles
				idx_pwm = chamber['pwm']
				dutys[idx_pwm] = chamber['obj'].calcControl(self.system_params['control'])
		else:
			dutys = [0]*self.n_chambers #TODO: some duties should be 100 to vent chambers
			
		# print(t, dutys) #DEBUG
		# ~ if not self.debug_gui:
			# ~ for idx, duty in enumerate(dutys):
				# ~ self.pwm.set_pwm(idx, duty) # update duty cycles


	def systemDisplayUpdate(self,t):
		self.label_t_run.setText(str(round(t/60,1))) # (min) update run time


	def logUpdate(self,t):
		# Log data into array
		self.data[self.n_samples,0] = t # record time
		self.data[self.n_samples,1:] = self.pressures # record pressures
		self.n_samples = self.n_samples + 1 # update number of samples

		if (self.data.shape[0] - self.n_samples) < 10:
			added_samples = round(self.system_params['freq']['log']*60*60) # add 1 hour
			self.data = np.append(self.data, np.zeros((added_samples,self.n_chambers+1), dtype=float), axis=0)
			print('append')
			print(self.data.shape)

	def saveLog(self):
		header = [None]*(self.n_chambers+1)
		header[0] = 'time (s)'
		for name, chamber in self.chambers.items(): # pressures logged in order of ADC
			idx_adc = chamber['adc']
			header[idx_adc+1] = name + ' (psi)'
		header = ', '.join(header)

		dirname = os.path.expanduser('~/Desktop/data')
		if not os.path.isdir(dirname):
			os.mkdir(dirname)
		filename = self.datetime_start.strftime("%Y-%m-%d_%H-%M-%S")
		np.savetxt(os.path.join(dirname, filename + '.txt'), self.data, delimiter = ', ',
			fmt='%0.2f', header=header)


	def updateTiming(self):
		self.thread_idle.stop()
		while not self.thread_idle.isFinished(): continue # wait until finished
		self.thread_idle.sense_freq = self.system_params['freq']['sense']
		self.thread_idle.display_freq = self.system_params['freq']['display']
		self.thread_idle.start()

		was_running = False
		if self.thread_run.isRunning():
			was_running = True
			self.thread_run.stop()
			while not self.thread_run.isFinished(): continue # wait until finished
		self.thread_run.control_freq = self.system_params['freq']['control']
		self.thread_run.display_freq = self.system_params['freq']['display']
		self.thread_run.log_freq = self.system_params['freq']['log']
		if was_running:
	 		self.thread_run.start()

		if not self.debug_gui:
			self.pwm.set_pwm_frequency(self.system_params['freq']['pwm'])


	def closeEvent(self, event):
		if self.run_on is True:
			self.stop() # stop run thread if running
		self.signal_stop_idle.emit() # stop idle thread
		if not self.debug_gui:
			self.GPIO.cleanup()
		if self.plot:
			self.plot_window.close()
		if self.tune:
			self.tune_window.close()
		print('closing') #
		event.accept()



############################################################
class PlotThread(QtCore.QThread):
	# When running: update plots
	signal_plot = QtCore.pyqtSignal(float)

	def __init__(self, plot_window, plot_freq):
		QtCore.QThread.__init__(self)
		self.running = False
		self.plot_freq = plot_freq		


	def stop(self):
		print('stop plot thread')
		self.running = False


	def run(self):
		# Loop:
		self.running = True
		t_plot = 0.0
		t_now = time.time
		t_start = t_now() # get start time
		while self.running:
			t = t_now() - t_start
			if t >= (t_plot + 1/self.plot_freq):
				self.signal_plot.emit(t) # emit sensor update signal
				t_plot = t # update plot time
				# print('plot update')



############################################################
class IdleThread(QtCore.QThread):
	# While app is running: sense pressures & update pressure displays
	signal_sense = QtCore.pyqtSignal(float)
	signal_display = QtCore.pyqtSignal(float)

	def __init__(self, sense_freq, display_freq):
		QtCore.QThread.__init__(self)
		self.running = False
		self.sense_freq = sense_freq
		self.display_freq = display_freq


	def stop(self):
		self.running = False


	def run(self):
		# Loop: sense pressures & update pressure displays
		self.running = True
		t_sensor = 0.0
		t_display = 0.0
		t_now = time.time
		t_start = t_now() # get start time
		while self.running:
			t = t_now() - t_start
			if t >= (t_sensor + 1/self.sense_freq):
				self.signal_sense.emit(t) # emit sensor update signal
				# print('sense: ', t-t_sensor) #DEBUG
				t_sensor = t # update sensor time

			t = t_now() - t_start
			if t >= (t_display + 1/self.display_freq):
				self.signal_display.emit(t)
				# print('display: ', t-t_display) #DEBUG
				t_display = t # update display time
				



############################################################
class RunThread(QtCore.QThread):
	# When running: update control, log data, & update system display
	signal_control = QtCore.pyqtSignal(float)
	signal_display = QtCore.pyqtSignal(float)
	signal_log = QtCore.pyqtSignal(float)

	def __init__(self, control_freq, display_freq, log_freq):
		QtCore.QThread.__init__(self)
		self.running = False
		self.control_freq = control_freq
		self.display_freq = display_freq
		self.log_freq = log_freq


	def stop(self):
		self.running = False


	def run(self):
		# Loop: update control, system display, & log
		self.running = True
		t_control = 0.0
		t_display = 0.0
		t_log = 0.0
		t_now = time.time
		t_start = t_now() # get start time
		while self.running:
			t = t_now() - t_start
			if t >= (t_control + 1/self.control_freq):
				self.signal_control.emit(t)	# emit control update signal
				# print('control: ', t-t_control) #DEBUG
				t_control = t # update control time

			t = t_now() - t_start
			if t >= (t_display + 1/self.display_freq):
				self.signal_display.emit(t) # emit display update signal
				# print('display: ', t-t_display) #DEBUG
				t_display = t # update display time
				
			t = t_now() - t_start
			if t >= (t_log + 1/self.log_freq):
				self.signal_log.emit(t) # emit log update signal
				# print('log: ', t-t_log) #DEBUG
				t_log = t # update log time






# value limit reminders
# killswitch interface for valves/pump --> talk to Drew

# nice to have
# 	status of killswitch
#	diagram of body/highlighting of active chambers
# 	touchpad?




# pyuic5 designer/mainwindow.ui -o package/ui/mainwindow.py
