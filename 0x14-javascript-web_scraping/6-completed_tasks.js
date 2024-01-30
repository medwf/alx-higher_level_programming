#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const URL = process.argv[2];
  request(URL, (error, res, body) => {
    if (error) {
      console.log(error);
    } else {
      res = JSON.parse(body);
      const data = {};
      for (let i = 0; i < res.length; i++) {
        if (res[i].completed && data[res[i].userId] === undefined) {
          data[res[i].userId] = 1;
        } else if (res[i].completed) {
          data[res[i].userId] += 1;
        }
      }
      console.log(data);
    }
  });
}
