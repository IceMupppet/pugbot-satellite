// Global Variables for Serial Port, Baud rate, Socket Port

var SERIAL_PORT = "/dev/ttyO2";
var BAUD_RATE   = 115200;
var SOCKET_PORT = 8001;

// Hardcoded API command to get out of Factory Mode and into UserHack Mode
var smu = [0xFF, 0xFF, 0x02, 0x42, 0x50, 0x02, 0x01, 0x68];
var l0 =  [0xFF, 0xFF, 0x02, 0x02, 0x71, 0x02, 0x01, 0x87];
 
var ws = require("nodejs-websocket")

var serialport = require('serialport'),
    SerialPort = serialport.SerialPort, 
      portName = "/dev/ttyO2";

var Sphero = new SerialPort(portName, {
   baudRate: 115200,
   parser: serialport.parsers.readline("\r\n")
 });

Sphero.on('open', sendSetUserHackMode);
 
var server = ws.createServer(function (socket_traffic) {

    console.log(" - Connection Started: ")

    var api_buf = [0xFF, 0xFF, 0x02, 0x20, 0x00, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00];

    function updatePacketToCommand_roll(speed, heading){
    	    api_buf[3]  = 0x30 							& 0xFF;
		    api_buf[6]  = speed 						& 0xFF;
		    api_buf[7]  = (heading >> 8)				& 0xFF; 
		    api_buf[8]  = heading 						& 0xFF; 
		    api_buf[9]  = 0x02 							& 0xFF;
		    api_buf[10] = 0x00 							& 0xFF;
		    api_buf[10] = calculateChecksum(api_buf) 	& 0xFF;
    }

    function calculateChecksum(aBuffer) {
  		var calculatedChecksum = 0;
		for (var _i = 0; _i < aBuffer.length; _i++) {
		  calculatedChecksum += aBuffer[_i];
		}
		calculatedChecksum = (calculatedChecksum + 2 & 0xFF) ^ 0xFF;
		return calculatedChecksum;
	};

	function displayPacket(packet){
		var hexString = "";
		for (var i = 0; i < packet.length; i++) {
			hexString += packet[i].toString(16);
		};
		return hexString;
	}

    // Parse packets from the socket connection send by virtualjoystick.js
    socket_traffic.on("text", function (str) {
        
        // Roll Command
		if(str.indexOf('roll') !== -1){
			var res = str.split(":");

			updatePacketToCommand_roll(res[1], res[2]);

			console.log("Roll Command : Heading [" + res[1] + "] Speed [" + res[2] + "]")

			console.log(displayPacket(api_buf));
                           
			Sphero.write(api_buf);

		}
		// RGB Command
		else if(str.indexOf('rgb') !== -1){
			var res = str.split(":");
			console.log("RGB Command  : R[" + res[1] + "] G["+ res[2]+"] B["+ res[3] + "]")
		}
		// Invalid Command
		else{
			console.log("Invalid command: " + str)
		}

    })

   socket_traffic.on("error", function (err) {
         console.log(" - Connection Ended:")
    })

}).listen(8001)

function sendSetUserHackMode() {
   //Sphero.write(smu);
   Sphero.write(l0);
}

console.log("Socket server listening on port 8001")
