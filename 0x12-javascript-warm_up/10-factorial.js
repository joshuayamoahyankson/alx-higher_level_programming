#!/usr/bin/node

const firstArg = process.argv[2];
const argInt = parseInt(firstArg);

if (isNaN(argInt)) {
  console.log(1);
} else {
    function fact(n) {
      if (n < 0) {
        return (1);
    } else if (n == 0) {
      return (1);
    }
    return (n * fact(n - 1));
  }
  console.log(fact(argInt));
}
