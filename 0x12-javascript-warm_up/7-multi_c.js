#!/usr/bin/node

const firstArg = process.argv[2];
const numInt = parseInt(firstArg);
let i = 0;

if (isNaN(numInt)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < numInt; i++) {
    console.log('C is fun');
  }
}
