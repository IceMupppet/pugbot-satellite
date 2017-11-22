var express = require('express');
var router = express.Router();

var serialport = require('serialport'),// include the library
   SerialPort = serialport.SerialPort, // make a local instance of it
   portName = "/dev/ttyO1";

var myPort = new SerialPort(portName, {
   baudRate: 115200,
   parser: serialport.parsers.readline("\r\n")
 });


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/forward', function(req,res){
   myPort.write("smu\r\n");
   myPort.write("\r\n");
   myPort.write("lc 128 0 0\r\n");
   myPort.write("\r\n");
   myPort.write("mf 255\r\n");
   res.render('index', {title: 'FORWARD' });
});


router.get('/reverse', function(req,res){
   myPort.write("smu\r\n");
   myPort.write("lc 255 0 128\r\n");
   myPort.write("mf 0\r\n");
   res.render('index', {title: 'REVERSE' });
});


module.exports = router;
