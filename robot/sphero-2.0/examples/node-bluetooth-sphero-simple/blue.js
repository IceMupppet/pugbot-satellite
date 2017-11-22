var spheron = require('spheron');
var sphero = spheron.sphero();
var spheroPort = '/dev/cu.Sphero-RRY-AMP-SPP';

var COLORS = spheron.toolbelt.COLORS;

sphero.on('open', function() {
  sphero.setRGB(COLORS.BLUE, false);
});

sphero.open(spheroPort);
