from pca9685_driver import Device
import time

if __name__=="__main__":
	dev = Device(0x40)
	dev.set_pwm_frequency(45) # (24- Hz)
	dev.set_pwm(0, 2047)
	dev.set_pwm(1, 2047)
	dev.set_pwm(2, 2047)
	dev.set_pwm(3, 2047)
	# ~ dev.set_pwm(12, 2047) # (0-4095 counts)
	# ~ dev.set_pwm(1, 2047) # (0-4095 counts)
	# ~ dev.set_pwm(2, 2047) # (0-4095 counts)
	# ~ dev.set_pwm(3, 2047) # (0-4095 counts)

	# ~ time.sleep(3)
	# ~ dev.set_pwm(0, 0)
	
	while True:
		# ~ dev.set_pwm(0, 0)
		# ~ time.sleep(1)
		# ~ dev.set_pwm(0, 2047)
		# ~ time.sleep(1)
		# ~ dev.set_pwm(0, 4096)
		time.sleep(1)





# ~ # sudo apt-get install python3-smbus


# ~ import smbus


# ~ i2c_channel = 1 #TODO

# ~ i2c_address = 0x00 #TODO

# ~ # register addresses


# ~ class Pwm:
	# ~ def __init__(self, i2c_channel, i2c_address):


		# ~ self.i2c_address
		# ~ self.bus = smbus.SMBus(i2c_channel) # initialize I2C




	# ~ def updateAll(self, dutys):
		# ~ # Update all duty cycles

		# ~ #TODO: loop over pressure channels:

		# ~ self.bus.write_i2c_block_data(self.i2c_address, reg, val)




# ~ #DEBUG: 
# ~ if __name__=="main":
	# ~ import time
	# ~ import numpy as np

	# ~ pwm = Pwm(i2c_channel, i2c_address)

	# ~ dutys = np.array([0,0,0,0])
	# ~ while True:
		# ~ dutys = dutys + 10
		# ~ for i, duty in enumerate(dutys):
	     	# ~ if duty > 100:
	            # ~ dutys[i] = 0


		# ~ pwm.updateAll(dutys)
		# ~ time.sleep(1)




