#!/usr/bin/node

if (Number(process.argv[2])) {
  const input = Number(process.argv[2]);
  let x;
  for (x = 0; x < input; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrances');
}
