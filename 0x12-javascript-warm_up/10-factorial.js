#!/usr/bin/node

const x = Number(process.argv[2]);
function fact (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
console.log(fact(x));
