#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const URL = process.argv[2];
  request(URL, (error, responde, body) => {
    if (error) {
      console.error(error);
    } else {
      const results = JSON.parse(body).results;
      let res = 0;
      // loop for every movie
      for (let movies = 0; movies < results.length; movies++) {
        // loop for every char
        for (let char = 0; char < results[movies].characters.length; char++) {
          if (results[movies].characters[char].endsWith('/18/')) {
            res++;
          }
        }
      }
      console.log(res);
    }
  });
}
