#!/usr/bin/node
const big = process.argv.slice(2).map(Number);
const biggest = big.sort((a, b) => b - a);

if (big.length <= 1) {
  console.log(0);
} else {
  console.log(biggest[1]);
}
