/*
 *
 *
 *
 *
 */

#include "adc_ads79.hpp"
#include "msp.h"
#include "driverlib.h"

#include <stdio.h>
#include <stdlib.h>



/*SPI Master Configuration Parameter*/ 
const eUSCI_SPI_MasterConfig spiConfig = { //TODO
	EUSCI_B_SPI_CLOCKSOURCE_SMCLK,              // SMCLK Clock Source
	3000000,                                    // SMCLK = DCO = 3MHZ
	500000,                                     // SPICLK = 500khz
	EUSCI_B_SPI_MSB_FIRST,                      // MSB First
	EUSCI_B_SPI_PHASE_DATA_CHANGED_ONFIRST_CAPTURED_ON_NEXT,     // Phase TODO
	EUSCI_B_SPI_CLOCKPOLARITY_INACTIVITY_HIGH,  // High polarity //TODO
	EUSCI_B_SPI_3PIN                           // 3Wire SPI Mode
};

/*Selecting P1.5 P1.6 and P1.7 in SPI mode*/
GPIO_setAsPeripheralModuleFunctionInputPin(GPIO_PORT_P1,GPIO_PIN5 | GPIO_PIN6 | GPIO_PIN7,  GPIO_PRIMARY_MODULE_FUNCTION);

/*Configuring SPI in 3wire master mode*/
SPI_initMaster(EUSCI_B0_BASE,  &spiMasterConfig);

/*Enable SPI module*/
SPI_enableModule(EUSCI_B0_BASE);

/*Enabling interrupts*/
SPI_enableInterrupt(EUSCI_B0_BASE,  EUSCI_B_SPI_RECEIVE_INTERRUPT);
Interrupt_enableInterrupt(INT_EUSCIB0);
Interrupt_enableSleepOnIsrExit();



// global
Adc adc(EUSCI_B1_BASE, &spiConfig, spi_master);


int main(void) {
	MAP_WDT_A_holdTimer();
	MAP_Interrupt_disableMaster();

	// clock stuff



	int ss[2] = {GPIO_PORT_P1, GPIO_PIN6};
    adc.initSlave(ss);


    MAP_Interrupt_enableMaster();



    while(1) {
    	//TODO:

    	adc.read();
    }


}

//TODO: timer interrupt for sensor read

//TODO: timer interrupt for control update


/////////////////////////////////////////////////////

#ifndef ADC_ADS79_HPP_
#define ADC_ADS79_HPP_


#include "SPIMSP.h"
#include <driverlib.h>


class Adc : private SPIMSP {
	public:

	private:
		uint32_t base;
		eUSCI_SPI_MasterConfig config;
		bool mode;
		int ss;
}


Adc::Adc(uint32_t base_, const eUSCI_SPI_MasterConfig* config_, bool mode_, int* ss_) {
	Adc::base = base_;
	Adc::config = *config_;
	Adc::mode = mode_;
	Adc::ss = ss_:
}



Adc::write16(uint16_t* tx_msg16) {
	/* write 2 bytes */
	uint8_t tx_msg8msb = (uint8_t)(tx_msg16 >> 8); // most significant byte
	uint8_t tx_msg8lsb = (uint8_t)(tx_msg16 & 0xFF); // least significant byte
	
	uint8_t tx_msg[2] = {tx_msg8msb, tx_msg8lsb}; // put bytes in message array
	Adc::write(Adc.ss, tx_msg, 2); // write bytes
}

Adc::read16(uint16_t* tx_msg16, uint16_t* rx_msg16) {
	/* read 2 bytes */
	uint8_t tx_msg8msb = (uint8_t)(tx_msg16 >> 8); // most significant byte
	uint8_t tx_msg8lsb = (uint8_t)(tx_msg16 & 0xFF); // least significant byte
	
	uint8_t tx_msg[2] = {tx_msg8msb, tx_msg8lsb}; // put bytes in message array
	uint8_t rx_msg[2];
	Adc::writeThenRead(Adc.ss, tx_msg, 2, rx_msg, 2)

	uint16_t rx_msg16 = (rx_msg[1] << 8) | (rx_msg[2]);
	rx_msg16 = rx_msg16 & ~0xF000; // remove top 4 bits

	//TODO: chop off top 4 bits


}

//      0111 0010 1101
// 0010 0111 0010 1101


Adc::init() {
	/* initialize ADC */
	Adc::write16(0x4200); // 0x4200 reset device (GPIO program register)
	Adc::write16(0x93C0); // 0x93C0 set last channel (Auto-2 program register)
	Adc::write16(0x3800); // 0x3800 Auto-2 mode; increment channel mode (Auto-2 mode register)
	Adc::write16(0x0000); // 0x0000 continued operation (Auto-2 mode control register)
	Adc::write16(0x0000); // 0x0000 continued operation (Auto-2 mode control register)
}


	    // int received_msg = ((uint16_t)byte_1 << 16) | (uint16_t)byte_2 << 8 | byte_3;


Adc::read() {


	

	Adc::writeThenRead(ss, uint8_t* tx_msg, int tx_len, uint8_t* rx_msg, int rx_len)


}




	void EUSCI_A_SPI_transmitData(uint32_t baseAddress,uint8_t transmitData); // transmit byte
	uint8_t EUSCI_A_SPI_receiveData (uint32_tbaseAddress); // receive byte


	while (!(MAP_SPI_getInterruptStatus(base, EUSCI_B_SPI_TRANSMIT_INTERRUPT)));
    MAP_SPI_transmitData(base, msg);
    while(MAP_SPI_isBusy(base));
    while (!(MAP_SPI_getInterruptStatus(base, EUSCI_B_SPI_RECEIVE_INTERRUPT)));
    uint8_t byte_1 = MAP_SPI_receiveData(base);
    while(MAP_SPI_isBusy(base));


    // int received_msg = ((uint16_t)byte_1 << 16) | (uint16_t)byte_2 << 8 | byte_3;


#endif /* ADC_ADS79_HPP */






