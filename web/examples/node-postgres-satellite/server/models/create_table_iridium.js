const pg = require('pg');
const connectionString = process.env.DATABASE_URL || 'postgres://icemupppet:pugbot-satellite@localhost:5432/pugbot';

const client = new pg.Client(connectionString);
client.connect();
const query = client.query('CREATE TABLE IRIDIUM(ID INT PRIMARY KEY NOT NULL,IMEI TEXT,MOMSN INT,TRANSMIT_TIME TIMESTAMP,LATITUDE REAL,LONGITUDE REAL,CEP INT,DATA TEXT)');
query.on('end', () => { client.end(); });
