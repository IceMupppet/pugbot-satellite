#Pug.io Node based joystick server using websockets


# Installation
Installation is currently just running both node express servers.

# Usage
The pug control scheme is setup in two parts.  A WebSocket node.js express server that runs locally on the pug, and a joystick that can reside either locally or remotely.  The joystick can be served by anything, in our example we use the express node.js server to host the joystick locally.

## Server (Local Pugbot)
The WebSocket Node.js Express server listens for websocket connections locally on the pug robot.  This uses the serial port to communicate with the Sphero board on `/dev/ttyO2` using the sphero Command API.

 * Default Port: 8001

     node pugio-socket-drive.js

You will know this is working when it is run, the control system is turned on and the board is set from factory mode to user hack mode. Now that the local robot is hosting it's websocket server, go host the joystick client.

### SpheroSocket Scripting SDK
The websocket Sphero SDK wrapper being used is simply the command and parameters delimanated by a colon (:), ie    

      command:param1:param2:param3


| command   | param1        | param2          | param3  | param4  |
|---------  |-------------- |---------------- |-------- |-------- |
| roll      | speed[0-100]  | heading[0-360]  |         |         |
|           |               |                 |         |         |
|           |               |                 |         |         |


## Joystick (Hosted Locally and on Pug.io)
The virtualjoystick is a javascript layer that was built mobile first to deal with multiple touches but also works with a simple mouse.  To serve this locally we use the express node.js server.

 * Default Port: 10001

     node serve-index.js

You must edit `index.html` and replace the websocket information with either the external ip address of the pug bot or the internal depending on where this is hosted.

    var socket = new WebSocket("ws://10.1.11.51:8001");

You can now access the pug bot joystick by viewing the `http://$IPADDRESS:10001` in any browser or tablet.

 * TODO:  Build a locate script to send this when starting the server.  

# Serving to the internet
If we want to drive this robot over the internet, we can easilly use `ngrok` which is pre-installed on pugbot.  Here we are hosting the joystick on a public server for easy acces.  (DigitalOcean Ubuntu Droplet) 

Start the server locally, then after everything is running, issue: 

     ngrok 8001

This will spit out a value forwared tunnel address for your pugbot.  Simply plug that in as the `socket` information located in `index.html` within the joystick folder.  start the server, or drop it into `/var/www/` if you are hosting that with `Apache2`. 

      node server-index.js

Visit the joystick with any browser or smartphone.
 
# Pug.io Webserver
Mentioned before, our public server is pug.io and is located at `http://107.170.231.48:10001`, if you access this with your webbrowser you should be in control of pug. SSH is available if your key is a known host in DigitalOcean.

      ssh root@107.170.231.48
