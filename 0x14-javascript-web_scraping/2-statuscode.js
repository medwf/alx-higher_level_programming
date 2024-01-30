#!/usr/bin/node

const request = require('request');

if (process.argv.length > 1) {
  const URL = process.argv[2];
  request(URL, (error, responce, body) => {
    if (error) {
      console.error(error);
    } else {
      console.log('code:', responce.statusCode);
    }
  });
}
