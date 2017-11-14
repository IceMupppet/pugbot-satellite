const pg = require('pg');
const connectionString = process.env.DATABASE_URL || 'postgres://icemupppet:pugbot-satellite@localhost:5432/template1';

const client = new pg.Client(connectionString);
client.connect();
const query = client.query('CREATE TABLE IRIDIUM(ID INT PRIMARY KEY NOT NULL,IMEI TEXT NOT NULL,MOMSN INT NOT NULL,TRANSMIT_TIME TIMESTAMP,LATITUDE REAL,LONGITUDE REAL,CEP INT,DATA TEXT)');
query.on('end', () => { client.end(); });
