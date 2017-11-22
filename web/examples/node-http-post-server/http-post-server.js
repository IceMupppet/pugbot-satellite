var express = require('express')
 , async = require('async')
 , http = require('http');

var bodyParser = require("body-parser");
var app = express();

app.set('port', process.env.PORT || 7002);

app.use(express.static(__dirname + '/public/images'));
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.post('/Details/',function(request,response,next){

   var userName     =request.body.username;
   var userEmail    =request.body.email;
   var userFirst    =request.body.firstName;
   var userLast     =request.body.lastName;

   console.log("Username: " + userName + " (" + userEmail +") Name: " + userFirst + " " + userLast);
} );


http.createServer(app).listen(app.get('port'), function(){
 console.log('Express server listening on port ' + app.get('port'));
});
