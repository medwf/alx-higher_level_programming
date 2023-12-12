#!/usr/bin/node
const Args = process.argv.slice(2);
const fs = require('fs').promises;
// console.log(Args);

const f1 = Args[0];
const f2 = Args[1];
const f3 = Args[2];

// console.log(f1, f2, f3);
try {
  const d1 = fs.readFile(f1);
  console.log(d1);
} catch (err) {
  console.log(err);
}
