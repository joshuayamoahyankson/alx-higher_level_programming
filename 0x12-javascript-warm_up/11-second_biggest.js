#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const numInt = args.map(arg => parseInt(arg));
  numInt.sort((a, b) => b - a);
  console.log(numInt[1]);
}
