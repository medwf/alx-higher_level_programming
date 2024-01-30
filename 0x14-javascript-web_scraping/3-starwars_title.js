#!/usr/bin/node

const request = require('request');

if (process.argv.length > 1) {
  const id = process.argv[2];
  const URL = 'https://swapi-api.alx-tools.com/api/films/' + id;
  request(URL, (error, responde, body) => {
    if (error) {
      console.error(error);
    } else {
      console.log(JSON.parse(responde.body).title);
    }
  });
}
