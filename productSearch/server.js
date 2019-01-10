'use strict';

const Hapi = require('hapi');
const Wreck = require('wreck');


const server = Hapi.server({
  port: 3000,
  host: 'localhost'
});

function getUri() {
  const uri = "http://api.walmartlabs.com/v1/items?apiKey=kjybrqfdgp3u4yv2qzcnjndj&format=json&ids=14225185,14225186"
  return uri
};

async function initialize () {

  const { res, payload } = await Wreck.get(getUri(), {json: true});

  server.route({
    method: 'GET',
    path: '/',
    handler: (r, h) => {
      return payload
    }
  });

  await server.start();
  console.log(`Server running at: ${server.info.uri}`);
};

process.on('unhandledRejection', (err) => {
  console.log(err);
  process.exit(1);
});

initialize();
