#!/usr/bin/env python3
import sys

import PyQt5
from PyQt5.QtWidgets import *

import mainwindow

class VestController(QMainWindow, mainwindow.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		self.on = False;

		chamber_names = ['aur', 'aul', 'alr', 'all'] # names of chambers
		self.chambers = dict() # dict of chambers
		for name in chamber_names:
			self.chambers[name] = PressureChamber(form, name) # instantiate PressureChamber for each chamber



        conn_sense, conn_control = mlt.Pipe(duplex=True) # set up multiprocessing pipe
	
		adc = Adc()
		self.pwm = Pwm()

		sense_process = mlt.Process(target=self.senseProcess, args=(adc, conn_sense))

		control_process = mlt.Process(target=)



		# signals & slots
		self.pushButton_on.clicked.connect(lambda: self.runSystem())



	def runSystem(self):
		if self.on is False:
			self.sense_process.start()
			self.control_process.start()
			self.on = True
			self.pushButton_on.setText('Off')
			print('running...')
		else: # self.on is True
			self.sense_process.stop()
			self.control_process.stop()
			self.on = False
			self.pushButton_on.setText('On')
			print('stopped!')



	def senseProcess(self):
		# t = 0
		# while True:
		# update time
		# if time to update (based on sense_frequency):
		# 	pressures = adc.read()
		# 	pipe pressures to control process
		# 	save pressures


	def controlProcess(self):
		# t = 0
		# while True:
		# 	update time
		# 	check for data in pipe, and update all chamber measurements if there is data
		

		# 	if time to update (based on control_frequency):
		# 		for all chambers:
		# 			chamber.updatePressure(pressure, t)



	def updateMeasurements(pressures):

		adc_map = {	'aur':0,
					'aul':1,
					'alr':2
					'all':3}

		for name, chamber in self.chambers.items():
			self.chamber.updateMeasurement(pressures[adc_map[name]])


	def updateControls():

		#TODO: pwm_map

		for chamber in self.chambers.values():
			duty = self.chamber.calcControl()




class PressureChamber:
	# Manage interaction between GUI signals & pressure control
	def __init__(self, form, chamber_name, control_freq):
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

		#TODO: instantiate pressure controller
		self.control = dict()
		self.control['freq'] = control_freq
		self.pres_meas = 0 # initialize pressure measurement
		self.pres_set = 0 # initialize pressure setpoint
		self.enabled = False

		self.controller = PressureController(control_freq)


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
			spin_val = self.spinbox.value()
			self.slider.setValue(round(spin_val*slider_max/spin_max,1))
		if n == 2: # slider updated
			slider_val = self.slider.value()
			self.spinbox.setValue(round(slider_val*spin_max/slider_max,1))

		# update controller
		#TODO: get setpoint from GUI
		self.controller.pres_set = pres_set


	def updateMeasurement(self, pressure): 
		self.controller.pres_meas = pressure
		#TODO: if time to update display (display_frequency): update display


	def calcControl(self):
		if self.form.on and self.enabled
			#TODO: control law
		else
			duty = 0
		return duty


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
	# instantiate GUI
	app = QApplication(sys.argv)
	form = VestController()
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