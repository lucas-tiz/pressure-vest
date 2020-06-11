#!/usr/bin/env python3

import spidev
import time


class Adc:
	def __init__(self, bus, device, last_channel):
		
		# parameters
		self.bus = bus
		self.device = device
		self.last_channel = last_channel # 0-15

		# registers
		self.gpio_prog_reg = 0b0100
		self.auto2_prog_reg = 0b1001
		self.auto2_mode_reg = 0b0011

		# set up & connect to SPI device
		self.spi = spidev.SpiDev()
		self.spi.open(self.bus, self.device) # bus, device
		self.spi.max_speed_hz=10000000  #10 MHz SPI clock speed TODO: make setable in init
		self.spi.cshigh=False
		self.spi.mode = 0b01 

		# configure ADC
		self.__writeData(self.gpio_prog_reg, 0b001000000000) # reset device (GPIO program register)

		last_channel_setting = (0b00 << 10) | (self.last_channel << 6) | (0b000000) 
		self.__writeData(self.auto2_prog_reg, last_channel_setting) # set last channel (Auto-2 program register)

		self.__writeData(self.auto2_mode_reg, 0b100000000000) # Auto-2 mode; increment channel mode (Auto-2 mode register)
			#TODO: also select Vref level here too

		self.__writeData(0x0, 0x000) # continued operation in Auto-2 mode to advance conversion channel
		self.__writeData(0x0, 0x000) # continued operation in Auto-2 mode to advance conversion channel

	def readAll(self):
		data = [0]*(self.last_channel+1)
		for i in range(self.last_channel):
			data[i] = self.__readData()

	def __readData(self):
		# Read ADC channel
		resp = self.spi.xfer2([0x00, 0x00]) # continued operation in Auto-2 mode, get response
		address_4bit = resp[0] >> 4 # channel address
		result = ((resp[0] & 0b1111) << 8) | resp[1] # conversion result
		return [address_4bit, result]


	def __writeData(self, register_4bit, setting_12bit):
		# Write settings to register
		msg_16bit = (register_4bit << 12) | setting_12bit # combine register & settings
		msbyte = msg_16bit >> 8 # split off most significant byte
		lsbyte = msg_16bit & 0xFF # split off least significant byte
		self.spi.writebytes2([msbyte, lsbyte])


		
# 0x4200 0100 0010 0000 0000

# 0x93C0 1001 0011 1100 0000

# 0x3800 0011 1000 0000 0000