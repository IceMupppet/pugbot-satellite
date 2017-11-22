var express = require('express');
var router = express.Router();
var spheron = require('spheron');
var sphero = spheron.sphero();
var spheroPort = '/dev/rfcomm0';
var COLORS = spheron.toolbelt.COLORS;


sphero.on('open', function() {
  sphero.setRGB(COLORS.GREEN, false);
});



/* GET home page. */
router.get('/', function(req, res, next) {
  
sphero.open(spheroPort);
   console.log("INDEX");
  res.render('index', { title: 'Express' });
});

router.get('/blue', function(req,res){
   console.log("BLUE");

  sphero.setRGB(COLORS.BLUE, false);
   res.render('index', {title: 'BLUE' });
});


router.get('/red', function(req,res){
   console.log("RED");

  sphero.setRGB(COLORS.RED, false);
   res.render('index', {title: 'RED' });
});


module.exports = router;
