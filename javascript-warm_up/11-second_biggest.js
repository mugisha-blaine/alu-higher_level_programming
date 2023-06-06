#!/usr/bin/node
function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) { return (0); }

  let big = myArray[2];
  let secondBig = myArray[3];

  for (let i = 2; i < myArray.length; i++) {
    if (myArray[i] > big) {
      secondBig = big;
      big = myArray[i];
    } else if (myArray[i] > secondBig && myArray[i] < big) {
      secondBig = myArray[i];
    }
  }
  return (secondBig);
}

console.log(second(process.argv));
