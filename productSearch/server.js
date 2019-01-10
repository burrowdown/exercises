'use strict';

const Hapi = require('hapi');


const server = Hapi.server({
  port: 3000,
  host: 'localhost'
});

function initialize () {

  server.route({
    method: 'GET',
    path: '/',
    handler: (r, h) => {
      return "test"
    }
  });

  server.start();
  console.log(`Server running at: ${server.info.uri}`);
};

process.on('unhandledRejection', (err) => {
  console.log(err);
  process.exit(1);
});

initialize();
