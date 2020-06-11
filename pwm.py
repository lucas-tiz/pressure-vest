


# sudo apt-get install python3-smbus


import smbus


i2c_channel = 1 #TODO

i2c_address = 0x00 #TODO

# register addresses


class Pwm:
	def __init__(self, i2c_channel, i2c_address):


		self.i2c_address
		self.bus = smbus.SMBus(i2c_channel) # initialize I2C




	def updateAll(self, dutys):
		# Update all duty cycles

		#TODO: loop over pressure channels:

		self.bus.write_i2c_block_data(self.i2c_address, reg, val)




#DEBUG: 
if __name__=="main":
	import time
	import numpy as np

	pwm = Pwm(i2c_channel, i2c_address)

	dutys = np.array([0,0,0,0])
	while True:
		dutys = dutys + 10
		for i, duty in enumerate(dutys):
	     	if duty > 100:
	            dutys[i] = 0


		pwm.updateAll(dutys)
		time.sleep(1)




