#!/usr/bin/node
const square = parseInt(process.argv[2]);
const fun = 'X';
if (!isNaN(square)) {
  console.log(fun*square);
} else {
  console.log('Missing size');
}
