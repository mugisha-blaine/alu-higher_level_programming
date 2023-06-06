#!/usr/bin/node
const square = parseInt(process.argv[2]);
const fun = 'X';
if (!isNaN(square)) {
  for (let i = 0; i < square; i++) {
    let times = ''
    for ( let j = 0; i < square; i++){
      console.log(`${message}${fun}`);
  }
} else {
  console.log('Missing number of occurrences');
}
