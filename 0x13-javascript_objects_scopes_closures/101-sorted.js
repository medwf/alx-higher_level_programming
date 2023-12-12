#!/usr/bin/node
const dc = require('./101-data').dict;

console.log(dc);
const New = {};
for (const key in dc) {
  if (New[dc[key]] === undefined) {
    New[dc[key]] = [];
  }
  New[dc[key]].push(key);
}
console.log(New);
