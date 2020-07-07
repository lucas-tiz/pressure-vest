#!/usr/bin/env python3
import os
import time
import ctypes

# ~ libbcm2835 = ctypes.CDLL(os.path.expanduser('~/Desktop/spi/libbcm2835.so'))
# ~ libbcm2835 = ctypes.CDLL('/root/Desktop/spi/libbcm2835.so')
libbcm2835 = ctypes.CDLL('/usr/local/lib/libbcm2835.so')

BCM2835_SPI_BIT_ORDER_MSBFIRST = ctypes.c_uint8(1)
BCM2835_SPI_MODE0 = ctypes.c_uint8(0)
BCM2835_SPI_CS0 = ctypes.c_uint8(0)



class Adc:
	def __init__(self, last_channel):
		self.last_channel = last_channel
		char2 = ctypes.c_char*2
		self.buf = char2(0x00, 0x00) 

		# registers
		self.gpio_prog_reg = 0b0100
		self.manual_mode_reg = 0b0001
		self.auto2_prog_reg = 0b1001
		self.auto2_mode_reg = 0b0011


		# configure SPI
		if not libbcm2835.bcm2835_init():
			print('init failed')

		if not libbcm2835.bcm2835_spi_begin():
			print('begin failed')

		libbcm2835.bcm2835_spi_begin()
		libbcm2835.bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST) # msByte first
		libbcm2835.bcm2835_spi_setDataMode(BCM2835_SPI_MODE0) # CPOL = 0, CPHA = 0 
		libbcm2835.bcm2835_spi_setClockDivider(ctypes.c_int16(32)) # 12.5 MHz SPI clock TODO: 32
		libbcm2835.bcm2835_spi_chipSelect(BCM2835_SPI_CS0) # chip select
		libbcm2835.bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, ctypes.c_uint8(0)) # chip select low


		# configure ADC
		self.__writeData(self.gpio_prog_reg, 0b001000000000) # reset device

		# self.__writeData(self.gpio_prog_reg, 0b000000001111) # set GPIOS as outputs

		last_channel_setting = (0b00 << 10) | (self.last_channel << 6)
		self.__writeData(self.auto2_prog_reg, last_channel_setting) # set last channel
			
		self.__writeData(self.auto2_mode_reg, 0b100001000000) # Auto-2 mode:...
			# increment channel mode, set Vref to 5V

		self.__writeData(0x0, 0x000) # continued operation in Auto-2 mode...
			# to advance conversion channel


	def readAll(self):
		''' Read all configured ADC channels '''
		data = []
		for i in range(self.last_channel+1):
			data.append(self.__readData())
		return data


	def __readData(self):
		''' Read ADC channel '''
		self.buf[:] = [0x00, 0x00] # update buffer with send data: continued operation in Auto-2 mode
		libbcm2835.bcm2835_spi_transfern(ctypes.byref(self.buf), ctypes.sizeof(self.buf)) # transfer data
		
		response = [int.from_bytes(self.buf[0], 'big'), int.from_bytes(self.buf[1], 'big')] # convert to ints
		address_4bit = response[0] >> 4 # channel address
		result = ((response[0] & 0b1111) << 8) | response[1] # conversion result
		return [address_4bit, result]
		

	def __writeData(self, register_4bit, setting_12bit):
		''' Write settings to register '''
		msg_16bit = (register_4bit << 12) | setting_12bit # combine register & settings
		msbyte = msg_16bit >> 8 # split off most significant byte
		lsbyte = msg_16bit & 0xFF # split off least significant byte

		self.buf[:] = [msbyte, lsbyte] # update buffer with send data
		libbcm2835.bcm2835_spi_transfern(ctypes.byref(self.buf), ctypes.sizeof(self.buf)) # transfer data


	def close(self):
		''' Reset SPI pins and close connection '''
		libbcm2835.bcm2835_spi_end()
		libbcm2835.bcm2835_close()



if __name__ == '__main__':
	last_channel = 7
	adc = Adc(last_channel)

	try:
		while True:
			t = time.time()
			data = adc.readAll()
			print(t-time.time())
			print(data)
			time.sleep(1)
	except KeyboardInterrupt:
		adc.close()
		print('done.')

