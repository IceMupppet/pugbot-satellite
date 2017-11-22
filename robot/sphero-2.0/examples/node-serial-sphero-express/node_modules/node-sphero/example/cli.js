var roundRobot = require('../');
var keypress = require('keypress');
var sphero = new roundRobot.Sphero();
var port = process.argv[2];

// make `process.stdin` begin emitting "keypress" events
keypress(process.stdin);

sphero.connect(port);

var quit = function(){
  sphero.close();
  process.stdin.pause();
  process.exit();
};

var color = function(){
  var r = Math.random()*255;
  var g = Math.random()*255;
  var b = Math.random()*255;
  return [r,g,b];
};

var keyCommands = {
  c: function(){
      var rgb = color();
      sphero.setRGBLED(rgb[0], rgb[1], rgb[2], false);
  },
  b: function(){
    sphero.setBackLED(1);
  },
  n: function(){
    sphero.setBackLED(0);
  },
  right: function(){
    sphero.setHeading(45);
  },
  left: function(){
    sphero.setHeading(315);
  },
  up: function(){
    sphero.roll(0, 0.5);
  },
  down: function(){
    sphero.roll(0, 0);
  },
  x: function(){
    sphero.setHeading(45).setHeading(315).setBackLED(1);
  },
  q: quit
};

sphero.on("connected", function(ball){
  console.log("Connected!");
  console.log("  c - change color");
  console.log("  b/n - back led on/off");
  console.log("  up - move forward");
  console.log("  back - stop");
  console.log("  left - change heading 45 deg left");
  console.log("  right - change heading 45 deg right");
  console.log("  q - quit");

  var rgb = color();
  sphero.setRGBLED(rgb[0], rgb[1], rgb[2], false);

  // listen for the "keypress" event
  process.stdin.on('keypress', function (ch, key) {
    if(!key) { return; }

    if (key.ctrl && key.name === 'c') {
      return quit();
    }

    if(keyCommands[key.name]){
      return keyCommands[key.name]();
    }
  });

  process.stdin.setRawMode(true);
  process.stdin.resume();

});

