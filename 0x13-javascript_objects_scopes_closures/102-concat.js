#!/usr/bin/node
const Args = process.argv.slice(2);
const fs = require('fs');

if (Args.length === 3) {
  const fileA = Args[0];
  const fileB = Args[1];
  const fileC = Args[2];
  /* console.log(fileA, fileB, fileC); */
  const fileAcontent = fs.readFileSync(fileA, 'utf8');
  const fileBcontent = fs.readFileSync(fileB, 'utf8');
  const concFile = fileAcontent + fileBcontent;
  fs.writeFileSync(fileC, concFile, 'utf8');
}
