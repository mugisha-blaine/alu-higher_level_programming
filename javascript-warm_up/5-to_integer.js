#!/usr/bin/node
const number = process.argv[2];
const convert = parseInt(number);
if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convert);
}
