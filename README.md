# PugBot Satellite 

The Main aspects to this project are as follows:  

1. The Robot
   * Chassis
   * Directional Control Board - *Sphero SPRK+ Board*
   		* Bluetooth LE
   			* Local Phone Control via BLE
   		* API Outputs: RGB LED, Vector Robot Control
   		* API Inputs: IMU Streaming Data, Ground Location
   * Main Processor - *Raspberry Pi 3*
   		* Ubuntu Linux
   		* Node.js, Express, VirtualJoystick.js
   		* Wifi Communication: WebSockets Server, Local Diagonstics
   		* Serial Communication:
   			* Port 1:  RockBLOCK (19002 Baud)
   			* Port 2:  Sphero API (115200 Baud)
   		* GPIO: Temperature, 
   	* Communication and GPS Data - *RockBLOCK SDB Radio* 
   		* API Inputs: imei, momsn, transmit_time, latitude, longitude, cep, data

2. The Webserver
	* Ubuntu Linux
   	* Node.js, PostgreSQL, Angular.js, Express, and Bootstrap
   	* RESTful API
   		* Coords : Last known Latitude, Longitude
   		* todos : list of all data packets from RockBLOCK Servers

   		


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

