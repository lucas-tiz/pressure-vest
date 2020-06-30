#!/usr/bin/env python3
from numpy import sign

class PressureChamber:
	# Manage interaction between GUI signals & pressure control
	def __init__(self, form, chamber_name):
		# GUI objects
		self.form = form
		self.groupbox = getattr(form, 'groupBox_' + chamber_name)
		self.frame = getattr(form, 'frame_' + chamber_name)
		# self.checkbox = getattr(form, 'checkBox_' + chamber_name)
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
		self.enabled = True
		self.pres_meas = 0 # initialize pressure measurement
		self.pres_set = 0 # initialize pressure setpoint
		self.err_int = 0 # initialize integral error
		self.err_prev = 0 # initialize previous error
		self.duty = {'inflation':0, 'deflation':0} #DEBUG


	def enableChamber(self):
		# Enable or disable pressure chamber
		if self.groupbox.isChecked() == 1:
			self.enabled = True # enable controller
			self.pres_set = self.spinbox.value() # setpoint to GUI value
		else:
			self.enabled = False # disable controller
			self.pres_set = 0 # setpoint to zero


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


	def calcControl(self, control):
		err = self.pres_meas - self.pres_set # (psi) pressure error

		if self.pres_set == 0: # if setpoint is zero
			if err > control['noise_threshold']: # and not within sensor noise range
				self.duty['inflation'] = 0 # fully close inflation valve
				self.duty['deflation'] = 100 # fully open vent valve
			else: # if within sensor noise range
				self.duty['inflation'] = 0 # fully close inflation valve
				self.duty['deflation'] = 0 # fully close vent valve
			self.err_int = 0 # reset integral

		elif (abs(err) <= control['differential_gap']): # if nonzero setpoint, but within differential gap
			self.duty['inflation'] = 0 # fully close inflation valve
			self.duty['deflation'] = 0 # fully close vent valve
			self.err_int = 0 # reset integral

		else: # if nonzero setpoint, out of differential gap
			if err < 0: # if below setpoint
				mode = 'inflation'
				self.duty['deflation'] = 0 # close deflation valve
			else: # if above setpoint
				mode = 'deflation'
				self.duty['inflation'] = 0 # close inflation valve
			kp = control[mode]['kp']
			ki = control[mode]['ki']
			kd = control[mode]['kd']

			# calculate control variables
			self.err_int = self.err_int + err
			err_der = err - self.err_prev
			self.err_prev = err 

			# reset integral windup
			if (self.err_int*ki > control['windup_limit']):
				self.err_int = control['windup_limit']/ki
			elif (self.err_int*ki < -control['windup_limit']):
				self.err_int = -control['windup_limit']/ki

			# calculate control & impose saturation limits
			u = control['deadzone'] + (kp*err + ki*self.err_int + kd*err_der)*sign(err)
			self.duty[mode] = min(u, 100)

		return self.duty


	def updateMeasurementDisplay(self):
		# ~ print(self.pres_meas)
		pres_round = round(self.pres_meas,1)
		if pres_round >= 0:
			self.label.setText(str(abs(pres_round)))
		else:
			self.label.setText(str(pres_round))

