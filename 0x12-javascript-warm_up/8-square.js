#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let right = 0; right < size; right++) {
    let row = '';
    for (let side = 0; side < size; side++) row += 'X';
    console.log(row);
  }
}
