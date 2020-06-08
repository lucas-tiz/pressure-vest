#!/usr/bin/env python3
import sys
import numpy as np
import datetime
import time

import PyQt5
from PyQt5.QtWidgets import *

import mainwindow
# import adc
# import pwm


class VestController(QMainWindow, mainwindow.Ui_MainWindow):
	def __init__(self, chamber_info):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# attributes
		self.t_app_start = time.time()
		self.chamber_info = chamber_info
		self.n_chambers = len(chamber_info)
		self.on = False

		self.log_freq = 1 # (Hz) TODO: make external

		# objects
		# self.adc = Adc(bus, device, last_channel) #TODO: set adc props
		# self.pwm = Pwm()
		self.chambers = dict() # dict of chambers
		for name in chamber_info:
			self.chambers[name] = PressureChamber(form, name) # instantiate PressureChamber for each chamber

		# signals & slots
		self.pushButton_on.clicked.connect(lambda: self.updateSystemState())

		# start in idle state
		self.idleSystem()


	def updateSystemState(self):
		if self.on is False:
			self.on = True
			self.runSystem()
			self.pushButton_on.setText('Off')
			print('running...')
		else: # self.on is True
			self.sense_process.stop()
			self.control_process.stop()
			self.on = False
			self.pushButton_on.setText('On')
			print('stopped!')


	def runSystem(self):
		max_samples = self.log_freq*60*60 # (1 hour) TODO: allocate more rows if getting close to max
		self.data = np.zeros(max_samples,17) # allocate data array 
		n_sample = 0 # initialize number of data samples recorded

		t_sensor = 0.0
		t_control = 0.0
		t_display = 0.0
		datetime_start = datetime.datetime.now() # get start date & time

		t_now = time.time
		t_start = t_now() # get start time
		while self.on:
			t = t_now() - t_start
			if t >= (t_sensor + 1/sense_frequency):
				self.sensorUpdate()
				t_sensor = t # update sensor time
				n_sample = n_sample + 1 # update number of samples

			t = t_now() - t_start
			if t >= (t_control + 1/control_frequency):
				self.controlUpdate()
				t_control = t # update control time

			t = t_now() - t_start
			if t >= (t_display+ 1/display_frequency):
				self.displayUpdate()
				t_display = t # update display time

		#TODO: set duty cycles to zero
		#TODO: export data
		print('loop ended')

		self.idleSystem() # switch to idle mode


	def idleSystem(self):
		# loop continuously and do notihing
		while not self.on:
			continue
			time.sleep(0.1)
			print(time.time()-self.t_app_start, 'idling...')

		self.runSystem() # switch to run mode
		


	def sensorUpdate(self):
		# self.pressures = self.adc.readAll() # read pressures
		self.pressures = [1,2,3,4] #DEBUG


		for name, chamber in self.chambers.items(): # update chamber pressures
			chamber.updateMeasurement(self.pressures[self.chamber_info[name]['adc']])

		self.data[n_sample,0] = t # record time
		self.data[n_sample,1:] = pressures # record pressures


	def controlUpdate(self):		
		dutys = [0]*self.n_chambers 
		for name, chamber in self.chambers.items(): # calculate duty cycles
			dutys[self.chamber_info[name]['pwm']] = chamber.calcControl()

		# self.pwm.updateAll(dutys) # update duty cycles

		print(name,duty) #DEBUG


	def displayUpdate(self):
		for name, chamber in self.chambers.items(): # update chamber pressures
			chamber.updateMeasurementDisplay()



class PressureChamber:
	# Manage interaction between GUI signals & pressure control
	def __init__(self, form, chamber_name):
		# GUI objects
		self.form = form
		self.frame = getattr(form, 'frame_' + chamber_name)
		self.checkbox = getattr(form, 'checkBox_' + chamber_name)
		self.spinbox = getattr(form, 'doubleSpinBox_' + chamber_name)
		self.slider = getattr(form, 'horizontalSlider_' + chamber_name)

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
			self.controller.enabled = True # enable controller
		else:
			self.frame.setEnabled(False) # disable chamber GUI
			self.controller.enabled = False # disable controller


	def updateSetpoint(self, n):
		# Update chamber pressure setpoint

		# update GUI
		spin_max = self.spinbox.maximum()
		slider_max = self.slider.maximum()
		if n == 1: # spin box updated
			pres_set = self.spinbox.value()
			self.slider.setValue(round(pres_set*slider_max/spin_max,1))
		if n == 2: # slider updated
			pres_set = self.slider.value()
			self.spinbox.setValue(round(pres_set*spin_max/slider_max,1))

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