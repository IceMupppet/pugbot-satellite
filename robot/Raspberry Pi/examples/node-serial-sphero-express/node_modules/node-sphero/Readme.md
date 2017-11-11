# Node Sphero

## How to use

    npm install node-sphero

Connect your [Sphero](http://gosphero.com) to your laptop over bluetooth. At this time only OSX 10.8/OSX 10.9/Windows 7 has been tested. You will need at least

Add Sphero to your app:

```javascript
var roundRobot = require('node-sphero');
var sphero = new roundRobot.Sphero();

sphero.on('connected', function(ball) {
  ball.setRGBLED(0, 255, 0, false);
});

sphero.connect();
```

Run that and your sphero should turn #00FF00... green.

Check out the examples for more ideas.

### How to use with Linux

The sphero will connect as a standard rf serial port. This has been tested under Ubuntu linux but should work generally as bluetooth serial is well supported.

Scan for devices and connect to the sphero without a pin - you should then get a notification stating you're connected to probably /dev/rfcomm0

You can now pass in the argument port your sphero is connceted on:

```bash
node example/cli.js /dev/rfcomm0
```

This will force the sphero to connect to the right serial port as node-serialport will not scan for rf serial ports.

Note that you may have some permissions issues on older versions of Ubuntu. You can hack your udev rules or run your script using sudo dpending on your needs.

## Installing

Node Sphero relies on node-serialport to communicate with the Sphero. Node-serialport is currently compatible with Linux, OSX 10.8 and up and Windows 7 and up running Node v0.8 and up. If you have issues installing Node Sphero and the errors messages say it cannot install node-serialport. Please checkout their [installation section](https://github.com/voodootikigod/node-serialport#to-install) and then [open an issue with](https://github.com/voodootikigod/node-serialport/issues?state=open) that project.


## In Progress

The rest of the sphero bluetooth api functionality.

## Thanks

Awesome work by [Bradley Meck](https://github.com/bmeck) who built the initial version.
