var api_buf = [0xFF, 0xFF, 0x02, 0x02, 0x72, 0x02, 0x00, 0x87] 

var serialport = require('serialport'),// include the library
   SerialPort = serialport.SerialPort, // make a local instance of it
   portName = process.argv[2];

var myPort = new SerialPort(portName, {
   baudRate: 115200,
   parser: serialport.parsers.readline("\r\n")
 });

myPort.on('open', sendSetUserHackMode);


function sendSetUserHackMode() {
   myPort.write(api_buf);
}
