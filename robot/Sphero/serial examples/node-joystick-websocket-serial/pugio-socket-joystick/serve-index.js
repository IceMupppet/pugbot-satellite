var express    = require('express');
var bodyParser = require("body-parser");
var os = require('os');

var server = express();

server.use(express.static(__dirname + '/'));
server.use(bodyParser.urlencoded({ extended: false }));

var interfaces = os.networkInterfaces();
var addresses = [];
for (var k in interfaces) {
    for (var k2 in interfaces[k]) {
        var address = interfaces[k][k2];
        if (address.family === 'IPv4' && !address.internal) {
            addresses.push(address.address);
        }
    }
}


var port = 10001;
server.listen(port, function() {
    console.log('server listening on ' + addresses[0] + ':' + port );
});
