var express = require('express')
 , async = require('async')
 , http = require('http');

var fs = require('fs');

var bodyParser = require("body-parser");
var app = express();

app.set('port', process.env.PORT || 7002);

app.use(express.static(__dirname + '/public/images'));
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.post('/Details/',function(request,response,next){

   var serverLocation = request.body.serverlocation;

   fs.writeFile('server-location.tmp', serverLocation, function(err){
        if(err) throw err;
   });

   console.log("Location: " + serverLocation);
} );


http.createServer(app).listen(app.get('port'), function(){
 console.log('Express server listening on port ' + app.get('port'));
});
