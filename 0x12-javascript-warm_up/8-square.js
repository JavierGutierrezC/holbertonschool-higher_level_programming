#!/usr/bin/node

const square = Number(process.argv[2]);
if (!Number(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < square; x++) {
    console.log('X'.repeat(square));
  }
}
