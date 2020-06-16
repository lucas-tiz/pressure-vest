#!/usr/bin/env python3
import sys
import numpy as np
import datetime
import time


from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

from package.ui	import mainwindow
# from package import adc
# from package.pca9685_driver import device


############################################################
class VestController(QMainWindow, mainwindow.Ui_MainWindow):

	signal_stop_idle = QtCore.pyqtSignal()
	signal_stop_run = QtCore.pyqtSignal()

	def __init__(self, chamber_info):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.setWindowTitle("Pressure Vest Controller")

		self.sense_freq = 5 # (Hz) TODO: set value, make external
		self.display_freq = 5 # (Hz) TODO: set value, make external
		self.control_freq = 1 # (Hz) TODO: set value, make external
		self.log_freq = 1 # (Hz) TODO: set value, make external

		# main attributes
		self.run_on = False
		self.t_app_start = time.time()

		# system signals & slots
		self.pushButton_on.clicked.connect(lambda: self.switchSystemState())

		# instantiate ADC and PWM modules
		# self.adc = Adc(bus, device, last_channel) #TODO: set adc props
		# self.pwm = Pwm() #TODO: set up PWM
		
		# instantiate chambers
		self.chamber_info = chamber_info
		self.n_chambers = len(chamber_info)
		self.pressures = [0]*self.n_chambers # chamber pressures
		self.chambers = dict() # dict of chambers
		for name in chamber_info:
			self.chambers[name] = PressureChamber(self, name) # instantiate PressureChamber for each chamber

		# set up sensor idle thread
		self.thread_idle = IdleThread(self.sense_freq, self.display_freq) # instantiate thread object
		self.signal_stop_idle.connect(self.thread_idle.stop) # set up signal to stop thread
		self.thread_idle.signal_sense.connect(self.sensorUpdate) # connect sensor update signal
		self.thread_idle.signal_display.connect(self.sensorDisplayUpdate) # connect display update signal
		self.thread_idle.start() # start thread

		# set up control/log run thread		
		self.thread_run = RunThread(self.control_freq, self.display_freq, self.log_freq)
		self.signal_stop_run.connect(self.thread_run.stop) # set up signal to stop thread
		self.thread_run.signal_control.connect(self.controlUpdate)
		self.thread_run.signal_display.connect(self.systemDisplayUpdate)
		self.thread_run.signal_log.connect(self.logUpdate)


	def switchSystemState(self):
		if self.run_on is False:
			self.run()
		else: # self.run_on is True
			self.stop()


	def run(self):
		self.run_on = True
		self.pushButton_on.setText('Stop')
		self.pushButton_on.setStyleSheet("background-color: rgb(235, 64, 52);\n")
		print('running...') #DEBUG
		self.initLog() # initialize data log
		self.thread_run.start()


	def stop(self):
		self.run_on = False
		self.pushButton_on.setText('Run')
		self.pushButton_on.setStyleSheet("background-color: rgb(0, 190, 0);\n")
		print('stopped!') #DEBUG
		self.signal_stop_run.emit() # emit run stop signal
		self.controlUpdate(vent=True) # turn off all
		print(self.data[0:10,:]) #DEBUG
		# self.saveLog() TODO
		

	def initLog(self):
		# Initialize data array for logging pressure data
		max_samples = self.log_freq*60*60 # (1 hour) TODO: allocate more rows if getting close to max
		self.data = np.zeros((max_samples,self.n_chambers+1), dtype=float) # allocate data array 
		self.n_sample = 0 # initialize number of data samples recorded
		self.datetime_start = datetime.datetime.now() # get start date & time


	def sensorUpdate(self, t):
		# Read/convert pressures from ADC & update pressure of each chamber object
		# self.pressures = self.adc.readAll() # read pressures
		pressures = np.array([1.0,2.0,3.0,4.0]) + t*self.sense_freq #DEBUG

		for name, chamber in self.chambers.items(): # update chamber pressures
			idx_adc = self.chamber_info[name]['adc'] # ADC index of pressure chamber
			chamber.updateMeasurement(pressures[idx_adc]) # update chamber measurement
			self.pressures[idx_adc] = pressures[idx_adc] # update pressures in class (in order of ADC)


	def sensorDisplayUpdate(self,t):
		for chamber in self.chambers.values(): # update chamber pressures
			chamber.updateMeasurementDisplay()


	def controlUpdate(self, t=None, vent=False):
		if not vent: # if duty cycles not specified		
			dutys = [0]*self.n_chambers 
			for name, chamber in self.chambers.items(): # calculate duty cycles
				dutys[self.chamber_info[name]['pwm']] = chamber.calcControl()
		else:
			dutys = [0]*self.n_chambers #TODO: some duties should be 100 to vent chambers
			
		print(dutys) #DEBUG

		# self.pwm.updateAll(dutys) # update duty cycles


	def systemDisplayUpdate(self,t):
		self.label_t_run.setText(str(round(t/60,1))) # (min) update run time


	def logUpdate(self,t):
		# Log data into array
		self.data[self.n_sample,0] = t # record time
		self.data[self.n_sample,1:] = self.pressures # record pressures
		self.n_sample = self.n_sample + 1 # update number of samples


	# def saveLog(self):
	# 	#TODO: get header names from chamber dict


	def closeEvent(self, event):
		if self.run_on is True:
			self.stop() # stop run thread if running
		self.signal_stop_idle.emit() # stop idle thread
		print('closing') #
		event.accept()



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
				t_sensor = t # update sensor time

			t = t_now() - t_start
			if t >= (t_display + 1/self.display_freq):
				self.signal_display.emit(t)
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
				t_control = t # update control time

			t = t_now() - t_start
			if t >= (t_display + 1/self.display_freq):
				self.signal_display.emit(t) # emit display update signal
				t_display = t # update display time

			t = t_now() - t_start
			if t >= (t_log + 1/self.log_freq):
				self.signal_log.emit(t) # emit log update signal
				t_log = t # update log time



############################################################
class PressureChamber:
	# Manage interaction between GUI signals & pressure control
	def __init__(self, form, chamber_name):
		# GUI objects
		self.form = form
		self.frame = getattr(form, 'frame_' + chamber_name)
		self.checkbox = getattr(form, 'checkBox_' + chamber_name)
		self.spinbox = getattr(form, 'doubleSpinBox_' + chamber_name)
		self.slider = getattr(form, 'horizontalSlider_' + chamber_name)
		self.label = getattr(form, 'label_' + chamber_name)

		# GUI signals & slots
		self.spinbox.valueChanged.connect(
			lambda: self.updateSetpoint(1)) # spinbox update
		self.slider.valueChanged.connect(
			lambda: self.updateSetpoint(2)) # slider update
		self.checkbox.stateChanged.connect(self.enableChamber) # checkbox update

		# chamber attributes
		self.pres_meas = 0 # initialize pressure measurement
		self.pres_set = 0 # initialize pressure setpoint
		self.enabled = True
		self.duty = 0 #DEBUG


	def enableChamber(self):
		# Enable or disable pressure chamber
		if self.checkbox.isChecked() == 1:
			self.frame.setEnabled(True) # enable chamber GUI
			self.enabled = True # enable controller
		else:
			self.frame.setEnabled(False) # disable chamber GUI
			self.enabled = False # disable controller


	def updateSetpoint(self, n):
		# Update chamber pressure setpoint

		# update GUI
		self.spinbox.blockSignals(True)
		self.slider.blockSignals(True)

		spin_max = self.spinbox.maximum()
		slider_max = self.slider.maximum()
		if n == 1: # spin box updated
			pres_set = self.spinbox.value()
			self.slider.setValue(round(pres_set*slider_max/spin_max,1))
		if n == 2: # slider updated
			slider_val = self.slider.value()
			pres_set  = round(slider_val*spin_max/slider_max,1)
			self.spinbox.setValue(pres_set)

		self.spinbox.blockSignals(False)
		self.slider.blockSignals(False)

		# update setpoint
		self.pres_set = pres_set
		print(self.pres_set) #DEBUG


	def updateMeasurement(self, pressure): 
		self.pres_meas = pressure


	def calcControl(self):
		if self.enabled:
			self.duty = self.duty + 1 #DEBUG
			duty = self.duty #DEBUG
			#TODO: control law
		else:
			duty = 0

		return duty


	def updateMeasurementDisplay(self):
		self.label.setText(str(round(self.pres_meas,1)))







# value limit reminders
# killswitch interface for valves/pump --> talk to Drew

# nice to have
# 	status of killswitch
#	diagram of body/highlighting of active chambers
# 	touchpad?