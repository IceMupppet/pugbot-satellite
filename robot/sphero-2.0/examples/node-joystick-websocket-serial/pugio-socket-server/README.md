# The Pug.io WebSocket Server

This will host the socket server that listens on port `8001` locally on the pug bot.

# Accessing the pug.io socket server from a local browser

Start the virtualjoystick server that will communicate with the socket server.

# Accessing the pug.io socket server from the internet

you must first forward port 8001 using ngrok so we can fill this info into pug.io online server.

       ngrok 8001

Edit the index.html on pug.io webserver 


       ws = "ws://n5ab3ds3.ngrok.com"

And run the joystick, if everything works you will see debug information.


