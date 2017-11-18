# PugBot Satellite 

The Main aspects to this project are as follows:  

1. The Robot
   * Chassis
   * Directional Control - Sphero
   		* Bluetooth LE
   		* RGB LED
   		* Ground Location API 
   * Main Processor - Raspberry Pi 3
   		* Ubuntu Linux
   		* Node.js, Express, VirtualJoystick.js
   		* Wifi Communication: WebSockets Server, Local Diagonstics
   		* Serial Communication:
   			* Port 1:  RockBLOCK (19002 Baud)
   			* Port 2:  Sphero API (115200 Baud)
2. The Webserver
	* Ubuntu Linux
   	* Node.js, PostgreSQL, Angular.js, Express, and Bootstrap
   	* RESTful API
   		* Coords
   		* todos

   		


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

