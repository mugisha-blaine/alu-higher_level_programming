#!/usr/bin/node
// A script that display the status code of a GET request

const url = process.argv[2];
let request = require('request');
request(args[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else console.log('code:', response && response.statusCode);
});
