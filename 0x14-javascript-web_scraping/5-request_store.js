#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length > 3) {
  const URL = process.argv[2];
  const file = process.argv[3];

  request(URL, (error, response, body) => {
    fs.writeFile(file, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
    if (error) {
      console.error(error);
    }
  });
}
