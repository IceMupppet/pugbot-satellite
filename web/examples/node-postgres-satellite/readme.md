# PostgreSQL and NodeJS with RockBLOCK

This is a basic single page application built with Node, Express, Angular, and PostgreSQL.  This will create the proprer table and REST points to capture packets from the test delivery section of Rock7.com along with actual packets from the RockBLOCK.

## Quick Start

1. Clone the repo
1. Install dependencies: `npm install`
1. Start your Postgres server and create a database called **pugbot**
2. Create a new user **icemupppet** with password **pugbot-satellite**
1. Create the database tables: `node server/models/create_table_iridium.js`
1. Start the server: `$ npm start`

## REST Endpoints

```
  /api/v1/pugbot
       GET
       POST
       DELETE
  /api/v1/coords
       GET
```


## Project Architecture

```
  ├-- Client
      └-- Views
          ├-- index.html
      ├-- Javascripts
          ├-- app.js
      └-- Stylesheets
          ├-- style.css
  ├-- Server
      └-- Modules
          ├-- create_table_iridium.js
      └-- Routes
          ├-- index.js
  ├-- Test
  ├-- App.js
```


## Tests

This comes with a load test using [Apache Bench](http://httpd.apache.org/docs/2.2/programs/ab.html) that by default exercises the API endpoint for the `/api/v1/pugbot` service:

```sh
sh tests/load-test.sh
```

Using this load test it is possible to verify several things:

- that the database is using as many connections as expected (it polls
  PostgreSQL for the number of active connections while it runs)
- the performance of the combined system under different loads

