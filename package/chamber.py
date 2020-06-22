#!/usr/bin/env python3


class PressureChamber:
	# Manage interaction between GUI signals & pressure control
	def __init__(self, form, chamber_name):
		# GUI objects
		self.form = form
		self.groupbox = getattr(form, 'groupBox_' + chamber_name)
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
		self.groupbox.toggled.connect(self.enableChamber) # checkbox update

		# chamber attributes
		self.pres_meas = 0 # initialize pressure measurement
		self.pres_set = 0 # initialize pressure setpoint
		self.enabled = True
		self.duty = 0 #DEBUG


	def enableChamber(self):
		# Enable or disable pressure chamber
		if self.groupbox.isChecked() == 1:
			self.enabled = True # enable controller
		else:
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
		# print(self.pres_set) #DEBUG


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