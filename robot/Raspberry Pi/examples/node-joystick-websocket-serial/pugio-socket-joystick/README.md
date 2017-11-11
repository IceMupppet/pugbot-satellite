# The Pug.io Joystick Javascript and server

Running the joystick can be done from Apache or simply by running the local node webserver.  This is the prefered method because it will also be able to listen for REST local instructions in the future.


      node serve-index.js

This will start the server on port 10001 by default.  If you are running this on the internet pug.io webserver it will still be 10001 but you can redirect everything in `/var/www/` on port 80  to port 10001.


