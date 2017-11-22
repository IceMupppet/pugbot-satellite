# Sphero API

Sphero baud rate: 115200

## Sphero API

setModeUserHackAPI.js

    var smu = [0xFF, 0xFF, 0x02, 0x42, 0x50, 0x02, 0x01, 0x68];
    var l0 =  [0xFF, 0xFF, 0x02, 0x02, 0x72, 0x02, 0x00, 0x87] 
    var l1 =  [0xFF, 0xFF, 0x02, 0x02, 0x71, 0x02, 0x01, 0x87] 

 ## Shell Commands

setModeUserHack

    smu

RGB Command

   myPort.write("lc 0 0 128\r\n");

Motor command 0 for stop

   myPort.write("mf 0\r\n");


###  Checksum

        function calculateChecksum(aBuffer) {
  		var calculatedChecksum = 0;
		for (var _i = 0; _i < aBuffer.length; _i++) {
		  calculatedChecksum += aBuffer[_i];
		}
		calculatedChecksum = (calculatedChecksum + 2 & 0xFF) ^ 0xFF;
		return calculatedChecksum;
	};



