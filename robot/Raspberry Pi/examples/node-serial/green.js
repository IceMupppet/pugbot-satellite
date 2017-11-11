var serialport = require('serialport'),// include the library
   SerialPort = serialport.SerialPort, // make a local instance of it
   portName = process.argv[2];

var myPort = new SerialPort(portName, {
   baudRate: 115200,
   parser: serialport.parsers.readline("\r\n")
 });

myPort.on('open', showPortOpen);

function showPortOpen() {
   myPort.write("lc 0 200 0\r\n");
}
