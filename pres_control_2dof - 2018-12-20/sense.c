#include "header.h"

// convert encoder counts to angles, filter, and save
void sensorUpdate(void)
{
    int i,j; // initialize index vars

    // shift angle histories
    theta1[1] = theta1[0];
    theta2[1] = theta2[0];

    // convert encoder counts to angles and save as current angles (add negative to reverse encoder direction)
    theta1[0] = -((float)(encCounts[0])*DEG_PER_COUNT + THETA_1_OFFSET); // convert base wheel counts to angle
    theta2[0] = -((float)(encCounts[1])*DEG_PER_COUNT + THETA_2_OFFSET); // convert wheel offset counts to angle

    // get ADC conversions
    MAP_ADC14_toggleConversionTrigger(); // initiate a single conversion (trigger)
    while(MAP_ADC14_isBusy()); // wait until ADC conversion complete
    uint16_t res[14]; // initialize array for ADC results
    for (i = 0; i < 14; i++)
    {
        res[i] = ADC14->MEM[i];
    }

    // update pressures & perform pressure calculations (pressures correspond to A0 - A4)
    int iAdc;
    for (i = 0; i < NUM_PRES_SENSOR; i++) // loop over pressure sensors
    {
        // shift pressure histories
        for (j = 0; j < LPF_ORDER; j++) // loop over pressure history
        {
          pres[i][LPF_ORDER-j] = pres[i][LPF_ORDER-(j+1)]; // shift each value right (20 = 19, 19 = 18,...)
        }

        iAdc = presAdc[i]; // index corresponding to ADC channel used for pressure measurement
        if (iAdc == 4) { // TODO: this is for 100 psi transducer, swap this out with a 30 psi for consistency
            pres[i][0] = ((res[iAdc]/16383.0)*3.3 - 0.5)*25.0; // (psi) convert and update newest pressure value
        }
        else { // for 30 psi transducers
            pres[i][0] = ((res[iAdc]/16383.0)*3.3 - 0.5)*7.5; // (psi) convert and update newest pressure value
        }

        presFilt[i][1] = presFilt[i][0]; // shift filtered pressure histories

        // calculate filtered pressures
        presFilt[i][0] = 0; // reset current value to zero
        for (j = 0; j <= LPF_ORDER; j++) // loop over pressure history
        {
            presFilt[i][0] = presFilt[i][0] + lpfCoeffs[j]*pres[i][j]; // calculate filtered value
        }
    }

    // update light sensors (light sensors correspond to A5 - A12)
    for (i = 0; i < NUM_LIGHT_SENSOR; i++) // loop over light sensors
    {
        iAdc = lightAdc[i]; // index corresponding to ADC channel used for light measurement
        light[i] = res[iAdc]*(3.3/16383); // update light sensor value
    }
}


// sensor update timer interrupt routine
void TA1_0_IRQHandler(void) {
    MAP_Interrupt_disableMaster(); // disable interrupts
    sensorFlag = 1; // set flag to get sensor values
    MAP_Timer_A_clearCaptureCompareInterrupt(TIMER_A1_BASE, TIMER_A_CAPTURECOMPARE_REGISTER_0); // clear interrupt flag
    MAP_Interrupt_enableMaster(); // enable interrupts
}
