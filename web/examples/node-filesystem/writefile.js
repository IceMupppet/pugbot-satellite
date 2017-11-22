// writefile.js
var fs = require('fs');
fs.writeFile('fs.tmp', 'temp', function(err) {
  if (err) throw err;
});
