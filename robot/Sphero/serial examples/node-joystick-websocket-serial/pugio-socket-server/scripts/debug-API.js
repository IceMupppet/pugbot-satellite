// Global Variables

var SOCKET_PORT = 8001;

var ws = require("nodejs-websocket")
 
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
		for (var _i = 2; _i < aBuffer.length; _i++) {
		  calculatedChecksum += aBuffer[_i];
		}
		calculatedChecksum = (calculatedChecksum & 0xFF) ^ 0xFF;
		return calculatedChecksum;
	};

	function displayPacket(packet){
		var hexString = "";
		for (var i = 0; i < packet.length; i++) {
			hexString += (i > 0 ? ":0x" : "0x") + packet[i].toString(16);
		};
		console.log("API Command: " + hexString + "\n");
	}

    // Parse packets from the socket connection send by virtualjoystick.js
    socket_traffic.on("text", function (str) {
        
        // Roll Command
		if(str.indexOf('roll') !== -1){
			var res = str.split(":");

			updatePacketToCommand_roll(res[1], res[2]);

			console.log("Roll Command : Speed [" + res[1] + "] Heading [" + res[2] + "]");
			displayPacket(api_buf);
			
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

console.log("Socket server listening on port 8001")
