#!/usr/bin/node
const Args = process.argv.slice(2);
let number = parseInt(Args[0]);

if (isNaN(number)) {
	console.log("Not a number");
}
else {
	console.log("My number:", number);
}
