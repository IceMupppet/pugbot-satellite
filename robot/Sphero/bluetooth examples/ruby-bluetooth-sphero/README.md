# Connecting Pug to Sphero over bluetooth

##Finding your Sphero

     hcitool scan

Scanning ...
    00:06:66:4A:3F:4B   Sphero-RGW
This provides the MAC address for your Sphero

##Determine your bluetooth interface
     
      hcitool dev

Devices:
    hci0    74:DE:2B:93:E2:9B
It should be or similar to hci0 if yours is different substitute it for hci0 in the following commands.

##Binding to your Sphero

     sudo rfcomm bind hci0 00:06:66:4A:3F:4B

This should create a device for you, the default is /dev/rfcomm0 if this is not the case you might also need to run

     sudo rfcomm bind hci0 /dev/rfcomm0