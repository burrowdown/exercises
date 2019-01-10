'use strict';

const FS = require('fs');
const Hapi = require('hapi');
const Wreck = require('wreck');


const server = Hapi.server({
  port: 3000,
  host: 'localhost'
});

function getUri() {
  const uri_base = "http://api.walmartlabs.com/v1/items?apiKey=kjybrqfdgp3u4yv2qzcnjndj&format=json&ids=";
  let ids = FS.readFileSync('data_file.csv', 'utf8').replace(/\n/g, '');
  let uri = uri_base + ids;
  return uri
};

function searchProductsForKeyword(products, keyword) {
  let output = new Array()
  products.forEach((product) => {
    try {
      if (product.longDescription.includes(keyword)) {
        output.push(product.itemId);
      }
    }
    catch {
      // ignore products with no longDescription
    }
  })
  return output;
};

async function initialize () {

  const { res, payload } = await Wreck.get(getUri(), {json: true});

  server.route({
    method: 'GET',
    path: '/items/{keyword}',
    handler: (r, h) => {
      return searchProductsForKeyword(payload.items, r.params.keyword)
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
