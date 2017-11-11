# UART1 is connected to Pin 24 and Pin 26 on the Beaglebone black

This requires you have enabled UART1 in uEnv.txt, this can be done with 

     scripts/setup/enableUART1.sh

this should enable the serial line for UART1 at boot time.  (requires reboot)

     ls /dev/ttyO1
               
 * Notice it is tty*O*1 (as in the letter o) not 0.

