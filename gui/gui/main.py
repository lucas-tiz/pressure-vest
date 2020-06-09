#!/usr/bin/env python3
import sys
import numpy as np
import datetime
import time

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import mainwindow
# import adc
# import pwm


# https://stackoverflow.com/questions/22340230/python-pyqt-how-run-while-loop-without-locking-main-dialog-window

class VestController(QMainWindow, mainwindow.Ui_MainWindow):

	signal_off = QtCore.pyqtSignal()

	def __init__(self, chamber_info):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# attributes
		self.t_app_start = time.time()
		self.chamber_info = chamber_info
		self.n_chambers = len(chamber_info)
		self.on = False

		# self.sense_freq = 2 # (Hz) TODO: set value, make external
		# self.control_freq = 1 # (Hz) TODO: set value, make external
		# self.display_freq = 1 # (Hz) TODO: set value, make external
		self.log_freq = 1 # (Hz) TODO: set value, make external

		# objects
		# self.adc = Adc(bus, device, last_channel) #TODO: set adc props
		# self.pwm = Pwm()
		
		self.chambers = dict() # dict of chambers
		for name in chamber_info:
			self.chambers[name] = PressureChamber(self, name) # instantiate PressureChamber for each chamber

		# signals & slots
		self.pushButton_on.clicked.connect(lambda: self.updateSystemState())


		# set up control stuff
		self.pressures = [0]*self.n_chambers
		
		sense_freq = 0.5 # (Hz) TODO: set value, make external
		self.log_freq = 1 # (Hz) TODO: set value, make external
		control_freq = 1 # (Hz) TODO: set value, make external
		# self.display_freq = 1 # (Hz) TODO: set value, make external
		self.controller = Controller(sense_freq, self.log_freq, control_freq)

		# self.signal_off = QtCore.pyqtSignal()
		self.signal_off.connect(self.controller.stop)


		self.controller.signal_sense.connect(self.sensorUpdate)
		self.controller.signal_log.connect(self.logUpdate)


	def updateSystemState(self):
		if self.on is False:
			self.on = True
			self.pushButton_on.setText('Off')
			print('running...')
			self.initLog() # initialize data log
			self.controller.start() # start controller
		else: # self.on is True
			self.on = False
			self.pushButton_on.setText('On')
			print('stopped!')
			self.signal_off.emit() # emit controller off signal #TODO: rename signal
			print(self.data[0:10,:])
			# self.saveLog() TODO
		

	def initLog(self):
		# Initialize data array for logging pressure data
		max_samples = self.log_freq*60*60 # (1 hour) TODO: allocate more rows if getting close to max
		self.data = np.zeros((max_samples,self.n_chambers+1), dtype=float) # allocate data array 
		self.n_sample = 0 # initialize number of data samples recorded
		self.datetime_start = datetime.datetime.now() # get start date & time


	def sensorUpdate(self,t):
		# Read/convert pressures from ADC & update pressure of each chamber object

		# self.pressures = self.adc.readAll() # read pressures
		pressures = [1,2,3,4] #DEBUG

		for name, chamber in self.chambers.items(): # update chamber pressures
			idx_adc = self.chamber_info[name]['adc'] # ADC index of pressure chamber
			chamber.updateMeasurement(pressures[idx_adc]) # update chamber measurement
			self.pressures[idx_adc] = pressures[idx_adc] # update pressures in class (in order of ADC)

		print(t,self.pressures)


	def logUpdate(self,t):
		# Log data into array
		self.data[self.n_sample,0] = t # record time
		self.data[self.n_sample,1:] = self.pressures # record pressures
		self.n_sample = self.n_sample + 1 # update number of samples


	def controlUpdate(self):		
		dutys = [0]*self.n_chambers 
		for name, chamber in self.chambers.items(): # calculate duty cycles
			dutys[self.chamber_info[name]['pwm']] = chamber.calcControl()

		# self.pwm.updateAll(dutys) # update duty cycles

		print(name,dutys) #DEBUG


	def displayUpdate(self):
		for name, chamber in self.chambers.items(): # update chamber pressures
			chamber.updateMeasurementDisplay()


	# def saveLog(self):
	# 	#TODO: get header names from chamber dict


class Controller(QtCore.QThread):

	signal_sense = QtCore.pyqtSignal(float)
	signal_log = QtCore.pyqtSignal(float)
	signal_control = QtCore.pyqtSignal(float)

	def __init__(self, sense_freq, log_freq, control_freq):
		QtCore.QThread.__init__(self)

		self.on = False

		self.sense_freq = sense_freq
		self.log_freq = log_freq
		self.control_freq = control_freq


	def stop(self):
		self.on = False


	def run(self):
		self.on = True

		t_sensor = 0.0
		t_log = 0.0
		t_control = 0.0
		t_display = 0.0
		# datetime_start = datetime.datetime.now() # get start date & time

		# t_now = time.time
		# t_start = t_now() # get start time

		# while self.on:
		# 	t = t_now() - t_start
		# 	if t >= (t_sensor + 1/self.sense_freq):
		# 		pressures = self.sensorUpdate()
		# 		self.data[n_sample,0] = t # record time
		# 		self.data[n_sample,1:] = pressures # record pressures
		# 		t_sensor = t # update sensor time
		# 		n_sample = n_sample + 1 # update number of samples

		# 	t = t_now() - t_start
		# 	if t >= (t_control + 1/self.control_freq):
		# 		self.controlUpdate()
		# 		t_control = t # update control time

		# 	t = t_now() - t_start
		# 	if t >= (t_display+ 1/self.display_freq):
		# 		self.displayUpdate()
		# 		t_display = t # update display time

		# #TODO: set duty cycles to zero
		# #TODO: export data
		# print('loop ended')


		t_now = time.time
		t_start = t_now() # get start time

		while self.on:
			t = t_now() - t_start
			if t >= (t_sensor + 1/self.sense_freq):
				self.signal_sense.emit(t) # emit sensor update signal
				t_sensor = t # update sensor time

			t = t_now() - t_start
			if t >= (t_log + 1/self.log_freq):
				self.signal_log.emit(t) # emit sensor update signal
				t_log = t # update sensor time

			t = t_now() - t_start
			if t >= (t_control + 1/self.control_freq):
				self.signal_control.emit(t)	
				t_control = t # update control time


			time.sleep(0.1) #DEBUG




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

			# self.control = dict()
			# self.control['freq'] = control_freq
		self.pres_meas = 0 # initialize pressure measurement
		self.pres_set = 0 # initialize pressure setpoint
		self.enabled = False

			# self.controller = PressureController(control_freq)

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



def main():

	chamber_info = {'aur':{'adc':0, 'pwm':0}, #TODO: put this in main
					'aul':{'adc':1, 'pwm':1},
					'alr':{'adc':2, 'pwm':2},
					'all':{'adc':3, 'pwm':3} }

	# instantiate GUI
	app = QApplication(sys.argv)
	form = VestController(chamber_info)
	form.show()

	# # instantiate a PressureChamber for each chamber
	# chamber_names = ['aur', 'aul', 'alr', 'all'] # names of chambers
	# chambers = dict() # dict of chambers
	# for name in chamber_names:
	# 	chambers[name] = PressureChamber(form, name)

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()







	# def runSystem(self):
	# 	max_samples = self.log_freq*60*60 # (1 hour) TODO: allocate more rows if getting close to max
	# 	self.data = np.zeros((max_samples,self.n_chambers+1), dtype=float) # allocate data array 
	# 	n_sample = 0 # initialize number of data samples recorded

	# 	t_sensor = 0.0
	# 	t_control = 0.0
	# 	t_display = 0.0
	# 	datetime_start = datetime.datetime.now() # get start date & time

	# 	t_now = time.time
	# 	t_start = t_now() # get start time

	# 	while self.on:
	# 		t = t_now() - t_start
	# 		if t >= (t_sensor + 1/self.sense_freq):
	# 			pressures = self.sensorUpdate()
	# 			self.data[n_sample,0] = t # record time
	# 			self.data[n_sample,1:] = pressures # record pressures
	# 			t_sensor = t # update sensor time
	# 			n_sample = n_sample + 1 # update number of samples

	# 		t = t_now() - t_start
	# 		if t >= (t_control + 1/self.control_freq):
	# 			self.controlUpdate()
	# 			t_control = t # update control time

	# 		t = t_now() - t_start
	# 		if t >= (t_display+ 1/self.display_freq):
	# 			self.displayUpdate()
	# 			t_display = t # update display time

	# 	#TODO: set duty cycles to zero
	# 	#TODO: export data
	# 	print('loop ended')

	# 		# self.idleSystem() # switch to idle mode




	#TODO:
# class PressureController:
# 	def __init__(self, control_freq):
# 		self.control_freq = control_freq
# 		self.pres_meas = 0 # initialize pressure measurement
# 		self.pres_set = 0 # initialize pressure setpoint
# 		self.enabled = False

# 	def updateControl();
# 		if self.enabled is True:
# 			#TODO: control law
# 		else
# 			duty = 0
# 		return duty

# 	def enableControl():




"""
sense_frequency
control_frequency
display_frequency

instantiate MainWindow
instantiate Adc
instantiate 8x PressureChamber

create dict mapping ADC channel numbers to chamber names

create process for sensing:
	t = 0
	while True:
		update time
		if time to update (sense_frequency):
			pressures = adc.read()
			pipe pressures to control process
			save pressures

create process for control update:
	t = 0
	while True:
		update time
		check for data in pipe, and update all chamber measurements if there is data
	

		if time to update (control_frequency):
			for all chambers:
				chamber.updatePressure(pressure, t)

"""


















# class MainWindow(QMainWindow):
# 	def __init__(self, parent=None):
# 		super(self.__class__, self).__init__(parent)
# 		doubleSpinBox_chamber = QDoubleSpinBox()

# 		# main_frame = QWidget()
#   #       main_frame.setLayout(layout)

#   #       self.setCentralWidget(main_frame)




# chamber_aur = PressureChamber(form.frame_aur, form.checkBox_aur,
# 	form.doubleSpinBox_aur, form.horizontalSlider_aur) # anterior upper right chamber
# chamber_aul = PressureChamber(form.frame_aul, form.checkBox_aul,
# 	form.doubleSpinBox_aul, form.horizontalSlider_aul) # anterior upper left chamber
# chamber_alr = PressureChamber(form.frame_alr, form.checkBox_alr,
# 	form.doubleSpinBox_alr, form.horizontalSlider_alr) # anterior lower right chamber
# chamber_all = PressureChamber(form.frame_all, form.checkBox_all,
# 	form.doubleSpinBox_all, form.horizontalSlider_all) # anterior lower left chamber

# print(form.groupBox_alr)




# timer after start
# value limit reminders
# get rid of hundredth place
# check bladder on and gray out/set to zero if unchecked
# single on off button (color change? play/stop button)

# killswitch interface for valves/pump --> talk to Drew

# nice to have
# 	status of killswitch
#	diagram of body/highlighting of active chambers
# 	touchpad?