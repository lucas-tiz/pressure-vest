#include "header.h"

// send data over UART
void sendData(void) {
    char str[100]; // TODO: adjust string size based on amount of data sent
    sprintf(str,"%3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f\r\n",
            theta1[0], theta2[0],
            presFilt[0][0], presFilt[1][0], presFilt[2][0], presFilt[3][0], presFilt[4][0],
            //debugVar[0], debugVar[1], debugVar[2], debugVar[3],
            light[0], light[1], light[2], light[3], light[4], light[5], light[6], light[7]); // format string with data to send

//    sprintf(str,"%3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f %3.3f\r\n",
//            kPid[0][0], kPid[0][1],
//            kPid[0][2], kPid[0][3], kPid[1][0], kPid[1][1], kPid[1][2],
//            kPid[1][3], kPid[2][0], kPid[2][1], kPid[2][2], kPid[2][3], kPid[3][0], kPid[3][1], kPid[3][2], kPid[3][3]); // format string with data to send

    int i = 0;
    while (str[i] != 0x00) { // while not at end of string null byte
        MAP_UART_transmitData(EUSCI_A0_BASE, str[i]); // transmit byte
        while (MAP_UART_getInterruptStatus(EUSCI_A0_BASE, EUSCI_A_UART_TRANSMIT_INTERRUPT_FLAG) != EUSCI_A_UART_TRANSMIT_INTERRUPT_FLAG); // wait for transmission completion
        i++;
    }
    sendDataCount = 0; // reset sensor flag
}


// receive data over UART: eUSCI A module interrupt routine
void EUSCIA0_IRQHandler(void) {
    MAP_Interrupt_disableMaster(); // disable all interrupts
    static int iBuf = 0; // text buffer index

    // if receive interrupt flag
    if (MAP_UART_getInterruptStatus(EUSCI_A0_BASE, EUSCI_A_UART_RECEIVE_INTERRUPT_FLAG) == EUSCI_A_UART_RECEIVE_INTERRUPT_FLAG) {
        textBuf[iBuf] = MAP_UART_receiveData(EUSCI_A0_BASE); // access received data by reading RXBUF register; flag automatically cleared

        if (textBuf[iBuf] == ';') { // if semicolon received
            updateValuesFlag = 1; // set flag to update values
            iBuf = 0; // reset text buffer index to zero (clear buffer)
        }
        else { // if no carriage return received
            if (iBuf < UART_BUFFER_SIZE) { // if text buffer index is less than max, increment index
                iBuf++;
            }
            else { // otherwise, reset index to zero
                iBuf = 0;
            }
        }
    }
    MAP_Interrupt_enableMaster(); // enable all interrupts
}

