var fs = require('fs');
fs.readFile('fs.tmp', function(err, buf) {
  console.log(buf.toString());
});
