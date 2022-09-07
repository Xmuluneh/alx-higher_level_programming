#!/usr/bin/node
const inputArray = process.argv;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let newArray = inputArray.slice(2);

  let i;

  for (i = 0; i < newArray.length; i++) {
    for (let k = i + 1; k < newArray.length; k++) {
      if (newArray[i] > newArray[k]) {
        const temp = newArray[i];
        newArray[i] = newArray[k];
        newArray[k] = temp;
      }
    }
  }
  console.log(newArray[newArray.length - 2]);
}
