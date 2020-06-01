#ifndef HEADER_H
#define HEADER_H

#include <stdio.h>
#include <stdlib.h>
#include <msp.h>
#include "driverlib.h"

// function prototypes
void Enc_Config(void);
void configClocks(void);
void configPins(void);
void Analog_Config(void);
void configTimers(void);
void configUart(void);
void configInterrupts(void);
void startTimers(void);
void initEncoder(void);
void sensorUpdate(void);
void controlUpdate(void);
void updateValues(void);
void sendData(void);
void EUSCIA0_IRQHandler(void);
void TA2_0_IRQHandler(void);
void PORT3_IRQHandler(void);
void csvStringRead(int nVals, volatile uint8_t * strRead, volatile float * arrWrite);
void delay(int d);

// macros
#define SENSE_FREQ 100.0 // sensor update frequency TODO: determine this
#define SEND_DATA_COUNT 10 // number of sensor loops between each data send
#define CONTROL_FREQ 100.0 // control update frequency TODO: determine this
#define PWM_PERIOD 33333 // pulse-width modulation timer period
#define LPF_ORDER 20                 // order of FIR low-pass filter
#define THETA_1_OFFSET -3.56 //2.9 //-3.56 // (deg) offset between zero position and index pulse TODO: determine
#define THETA_2_OFFSET -29.18 //16.172 // (deg) offset between zero position and index pulse TODO: determine
#define NUM_PRES_SENSOR 5  // number of pressure sensors; 5 max based on number of provided PWM signals
#define NUM_LIGHT_SENSOR 8 // number of light sensors
#define DEG_PER_COUNT 360.0/8192.0 // encoder degrees per count
#define UART_BUFFER_SIZE 200 // UART text buffer size

// debug variables
extern volatile float debugVar[6];

////TODO: check where volatile actually needed - probably only for flags
// encoder variables
extern uint8_t encPins[2][3]; // encoder channel pins; 1 row per encoder
extern volatile int encCounts[2];        // encoder counts (encoder 1, encoder 2) TODO: create static var inside encoder func
extern volatile uint8_t prevEncState[2]; // previous states of both encoders (encoder 1, encoder 2) TODO: create static var inside encoder func

// sensor variables
extern float lpfCoeffs[LPF_ORDER+1]; // FIR low-pass filter coefficients
extern const int presAdc[NUM_PRES_SENSOR]; // ADC channel corresponding to pressure sensor
extern volatile float pres[NUM_PRES_SENSOR][LPF_ORDER+1]; // (psi) current and previous pressures
extern volatile float presFilt[NUM_PRES_SENSOR][2]; // (psi) current and one previous time-step of filtered pressures
extern const int lightAdc[NUM_LIGHT_SENSOR]; // ADC channel corresponding to light sensor
extern volatile float light[NUM_LIGHT_SENSOR]; // (V) current and previous light sensor values
extern volatile float theta1[2]; // (deg) current and previous proximal joint angles
extern volatile float theta2[2]; // (deg) current and previous distal joint angles
extern volatile int sensorFlag;      // sensor update flag

// control variables
extern float kPid[NUM_PRES_SENSOR][4]; // PID gains for pressure control channels
extern volatile float presDes[NUM_PRES_SENSOR]; // desired pressures
extern volatile int controlFlag; // control update flag
extern volatile int newSetpointFlag; // new pressure setpoint flag

// data reception & transmission variables
extern int sendDataCount; // UART data transmission counter TODO: create static var inside sensor function
extern volatile uint8_t textBuf[UART_BUFFER_SIZE]; // initialize text buffer
extern volatile int updateValuesFlag;

// timer configurations
extern const Timer_A_PWMConfig pwmTimerConfig1; // PWM timer
extern const Timer_A_PWMConfig pwmTimerConfig2; // PWM timer
extern const Timer_A_PWMConfig pwmTimerConfig3; // PWM timer
extern const Timer_A_PWMConfig pwmTimerConfig4; // PWM timer
extern const Timer_A_PWMConfig pwmTimerConfig5; // PWM timer
extern const Timer_A_UpModeConfig sensorTimerConfig; // sensor timer
extern const Timer_A_UpModeConfig controlTimerConfig; // control timer

// UART configuration
extern const eUSCI_UART_Config uartConfig;


#endif
