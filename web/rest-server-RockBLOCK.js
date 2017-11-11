var express = require('express')
 , async = require('async')
 , http = require('http');

var express = require('express');
var bodyParser = require('body-parser');
var app = express();

app.set('port', process.env.PORT || 7002);

app.use(express.static(__dirname + '/public/images'));
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.post('/Details/',function(request,response,next){

   var local_imei         =request.body.imei;
   var local_momsn        =request.body.momsn;
   var local_transmit     =request.body.transmit_time;
   var local_latitude     =request.body.iridium_latitude;
   var local_longitude    =request.body.iridium_longitude;
   var local_cep          =request.body.iridium_cep;
   var local_data         =request.body.data;

    var hex = local_data.toString();//force conversion
    var str = '';
    for (var i = 0; i < hex.length; i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));

   console.log("IMEI: " + local_imei + " (" + local_momsn +") @[ " + local_latitude + ", " + local_longitude + "] (" + local_transmit + ") : " + str);
   response.writeHead(200, {'Content-Type': 'text/html'});
   response.end();
} );


http.createServer(app).listen(app.get('port'), function(){
 console.log('Express server listening on port ' + app.get('port'));
});
