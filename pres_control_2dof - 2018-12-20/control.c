#include "header.h"


// update desired pressure setpoints from serial data
void updateValues(void) { // TODO: change function name and add functionality for multiple types of value updates
    // update desired pressures
    if (textBuf[0] == 'p') {
        csvStringRead(NUM_PRES_SENSOR, textBuf + 1, presDes); // convert text buffer to float array & update desired pressure array
        newSetpointFlag = 1; // set flag to indicate new setpoint received
    }

    // update pressure controller gains
    else if (textBuf[0] == 'k') {
        int iPres = textBuf[1] - '0'; // get index of pressure controller to update
        csvStringRead(4, textBuf + 2, kPid[iPres]); // convert text buffer to float array & update desired pressure array
    }
}


// PID pressure control: maintain desired pressure setpoints
void controlUpdate(void) {
    float err;
    static float errInt[NUM_PRES_SENSOR] = {0};
    float errDer;
    static float errPrev[NUM_PRES_SENSOR] = {0};
    float u;
    float duty;

    static float presDesPrev[NUM_PRES_SENSOR] = {0};

    // loop over pressure control inputs
    int i;
    for (i = 0; i < NUM_PRES_SENSOR-1; i++) {
        err = presFilt[i][0] - presDes[i]; // (psi) calculate pressure error

//        if (presDes[i] != presDesPrev[i]) {
//            errInt[i] = 0; // reset integral error for new setpoint
//        }
//        else {
//            errInt[i] = errInt[i] + err; // (psi-time) pressure integral error
//        }
//        presDesPrev[i] = presDes[i]; // (psi) set previous pressure setpoint to current setpoint

        errInt[i] = errInt[i] + err; // (psi-time) integrate pressure error
        errDer = err - errPrev[i]; // (psi/time) calculate pressure derivative
        errPrev[i] = err; // (psi) set previous error to current error

        // reset integral windup
        if (errInt[i]*kPid[i][1] > kPid[i][3]) {
            errInt[i] = kPid[i][3]/kPid[i][1];
        }
        else if (errInt[i]*kPid[i][1] < -kPid[i][3]) {
            errInt[i] = -kPid[i][3]/kPid[i][1];
        }



//        u = -kPid[i][0]*err - kPid[i][1]*errInt[i] - kPid[i][2]*errDer; // calculate raw controller input
//        u = kPid[i][0]*presDes[i] + 9.9 - kPid[i][1]*errInt[i] - kPid[i][2]*errDer;

//        duty = TIMER_A0->CCR[i+1] + (int)(PWM_PERIOD*(u/100.0)); // raw duty cycle in timer counts

//        duty = ((u+100.0)/2.0); // map input (-100 to 100 ish) to duty cycle (0 to 100)
//        duty = ((u+100.0))/200.0*(100.0-7.0) + 7.0; // map input (-100 to 100 ish) to duty cycle (7 to 100)


        // for free actuation testing
        u = (kPid[i][2]*presDes[i] + 10) - kPid[i][0]*err - kPid[i][1]*errInt[i] ; // input: ff + prop + int
        duty = u;

        // impose saturation limits
        if (duty > 100.0) {
            duty = 100.0;
        }
        else if (duty < 10.0) {
            duty = 0.0;
        }

        // if desired pressure is zero, just set duty cycle to zero immediately
        if (presDes[i] == 0) {
            duty = 0.0;
        }
        TIMER_A0->CCR[i+1] = (int)((duty/100.0)*PWM_PERIOD); // update PWM timer duty cycle

        debugVar[i] = duty;

        //TODO: for debug
//        TIMER_A0->CCR[1] = PWM_PERIOD;
//        TIMER_A0->CCR[3] = 0;
//        TIMER_A0->CCR[4] = 0;
    }

    // pump control
    if (presFilt[4][0] > 14) { // 10 for free actuation
        MAP_GPIO_setOutputLowOnPin(GPIO_PORT_P6, GPIO_PIN6 | GPIO_PIN7);// disable pumps
    }
    else if (presFilt[4][0] < 12) { // 8 for free actuation
        MAP_GPIO_setOutputHighOnPin(GPIO_PORT_P6, GPIO_PIN6 | GPIO_PIN7); // enable pumps
    }
}


// control update timer interrupt routine
void TA2_0_IRQHandler(void) {
    MAP_Interrupt_disableMaster(); // disable interrupts
    controlFlag = 1; // set flag to get update system control
    MAP_Timer_A_clearCaptureCompareInterrupt(TIMER_A2_BASE, TIMER_A_CAPTURECOMPARE_REGISTER_0); // clear interrupt flag
    MAP_Interrupt_enableMaster(); // enable interrupts
}

