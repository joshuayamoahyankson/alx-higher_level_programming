#!/usr/bin/node

const firstNum = parseInt(process.argv[2]);
const secondNum = parseInt(process.argv[3]);

function add (a, b) {
  console.log(firstNum + secondNum);
}
add(firstNum, secondNum);
