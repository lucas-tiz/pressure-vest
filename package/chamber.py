#!/usr/bin/env python3
from numpy import sign

class PressureChamber:
	''' Manage interaction between GUI signals & pressure control '''
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
		self.duty = {'inflate':0, 'deflate':0} #DEBUG


	def enableChamber(self):
		''' Enable or disable pressure chamber '''
		if self.groupbox.isChecked() == 1:
			self.enabled = True # enable controller
			self.pres_set = self.spinbox.value() # setpoint to GUI value
		else:
			self.enabled = False # disable controller
			self.pres_set = 0 # setpoint to zero


	def updateSetpoint(self, n):
		''' Update chamber pressure setpoint '''
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


	def calcControl(self, param):
		err = self.pres_meas - self.pres_set # (psi) pressure error

		if self.pres_set == 0: # if setpoint is zero
			if err > param['noise_threshold']: # and not within sensor noise range
				self.duty['inflate'] = 0 # fully close inflate valve
				self.duty['deflate'] = 0 # fully open deflate valve
			else: # if within sensor noise range
				self.duty['inflate'] = 0 # fully close inflate valve
				self.duty['deflate'] = 100 # fully close deflate valve
			self.err_int = 0 # reset integral

		elif (abs(err) <= param['differential_gap']): # if nonzero setpoint, but within differential gap
			self.duty['inflate'] = 0 # fully close inflate valve
			self.duty['deflate'] = 100 # fully close deflate valve
			self.err_int = 0 # reset integral

		else: # if nonzero setpoint, out of differential gap
			if err < 0: # if below setpoint
				mode = 'inflate'
				self.duty['deflate'] = 100 # close deflate valve
			else: # if above setpoint
				mode = 'deflate'
				self.duty['inflate'] = 0 # close inflate valve
			kp = param[mode]['kp']
			ki = param[mode]['ki']
			kd = param[mode]['kd']

			# calculate control variables
			self.err_int = self.err_int + err
			err_der = err - self.err_prev
			self.err_prev = err 

			# reset integral windup
			if (self.err_int*ki > param['windup_limit']):
				self.err_int = param['windup_limit']/ki
			elif (self.err_int*ki < -param['windup_limit']):
				self.err_int = -param['windup_limit']/ki

			# calculate control
			u = -(kp*err + ki*self.err_int + kd*err_der) # feedback control
			if mode is 'inflate': # add deadzone compensation
				u = param['deadzone'] + u 
			else: # (mode is deflate)
				u = (100 - param['deadzone']) + u
			u = u*(4095/100) # scale to 12-bit
			self.duty[mode] = max(0, min(u, 4095)) # impose saturation limits

		return self.duty


	def updateMeasurementDisplay(self):
		# ~ print(self.pres_meas)
		pres_round = round(self.pres_meas,1)
		if pres_round >= 0:
			self.label.setText(str(abs(pres_round)))
		else:
			self.label.setText(str(pres_round))

