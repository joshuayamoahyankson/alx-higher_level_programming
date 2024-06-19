#!/usr/bin/node

const firstArg = process.argv[2];
const size = parseInt(firstArg);
let i = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log(Array(size).fill('X').join(''));
  }
}
