//*****************************************************************************
//
// MSP432 main.c - 2-DOF linkage PAM control
//
// Lucas Tiziani
// 20 October 2017
//
//****************************************************************************

/* Program outline
 *
 *    - 5x ADC for pressure transducers (minimum)
 *    - 8x ADC for optical sensors
 *    - 6x external interrupts (3 per encoder)
 *    - 4x timers for PWM - can just use timer A0 for all 4 (has 5 capture/compare registers)
 *    - 1x timer for sensing loop
 *    - 1x timer for control loop
 *    - UART for communication with Python
 *
 */

#include "header.h"



void PORT3_IRQHandler(void);
void TA1_0_IRQHandler(void);
void TA2_0_IRQHandler(void);


void main(void) {
    MAP_WDT_A_holdTimer(); // hold the watchdog timer (stop from running)
    MAP_Interrupt_disableMaster(); // disable interrupts

    configClocks();
    configPins();
    configTimers();

    Analog_Config();
    Enc_Config();

    configUart();
    configInterrupts();
    startTimers();

    MAP_Interrupt_enableMaster(); // enable interrupts
    initEncoder(); // initialize encoders

    while(1) {
        if (sensorFlag) {
            sensorUpdate(); // get sensor data
            sensorFlag = 0; // clear sensor flag

            if (sendDataCount == 2) {
                sendData(); // send sensor data
                sendDataCount = 0; // reset sensor flag
            }
            sendDataCount++; // increment sensor flag
        }
        if (controlFlag) {
            controlUpdate(); // update control
            controlFlag = 0; // clear control flag
            MAP_GPIO_toggleOutputOnPin(GPIO_PORT_P2, GPIO_PIN0);

        }
        if (updateValuesFlag) {
            updateValues(); // update pressure setpoint values
            updateValuesFlag = 0; // clear values update flag
        }

        // Instron trigger
        if (presDes[3] == -1) {
            MAP_GPIO_setOutputHighOnPin(GPIO_PORT_P2, GPIO_PIN2);
            MAP_GPIO_setOutputHighOnPin(GPIO_PORT_P6, GPIO_PIN4); // trigger Instron test start
        }
        else {
            MAP_GPIO_setOutputLowOnPin(GPIO_PORT_P2, GPIO_PIN2);
            MAP_GPIO_setOutputLowOnPin(GPIO_PORT_P6, GPIO_PIN4); // reset trigger
        }
    }
}

