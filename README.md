# PugBot Satellite 

This project uses two (2) separate node.js webservers.  

### Hosted Webserver 
The first one is located on a hosted server. (in this case DigitalOcean) This server hosts RESTful endpoints to gather all data being sent to/from the Robot via Iridium Satellite SBD Rock7.com.  There are REST points for off loading sensor data from the Robot as well.  It hosts the Socket Server for the robot client to attach to that will allow the user to drive the robot (on Wifi) from anywhere that has internet using the Control page.  It also serves as the Dashboard, Location Tracking, and Control Module for the PugBot.

### Robot Webserver
This webserver is hosted on the robot iteself.  This server will host a Similar Control Page as that on the Hosted Webserver for local driving sent through Serial to the Sphero Board.  It will also host the Socket Client that attaches to the Hosted Server Websock server for control via the internet.  This Webserver maintains the local database of collected sensor data.

## Setup

## Usage

### Web Hosting for RockBLOCK data
This is hosted on an ubuntu linux server. Requires Node.js and Postgres.

````$ npm install -g express-generator@4.13.4````

````npm install supervisor@0.11.0 -g````

````$ npm start````

````$ npm install pg@6.1.0 --save````


### Apt-get repositories
````$ sudo apt-get install postgis unzip gdal-bin```` 

````$ sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable````

### Running postgres

````sudo -i -u postgres````

````psql -d template1````

***

#### psql commands
 **\d  - list the databases**
 
 **\dt - list the tables**
 
 **\du - list the users**
 
 ***

## Documents

