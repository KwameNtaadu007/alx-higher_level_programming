#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let fig = 0; fig < x; fig++) {
    console.log('C is fun');
  }
}
