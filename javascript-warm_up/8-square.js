#!/usr/bin/node
const square = parseInt(process.argv[2]);
const fun = 'X';
if (!isNaN(square)) {
  for (let i = 0; i < square; i++) {
    let times = '';
    for (let j = 0; j < square; j++) {
      times = times + fun;
    }
    console.log(times);
  }
} else {
  console.log('Missing size');
}
