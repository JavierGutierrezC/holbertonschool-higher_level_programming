#!/usr/bin/node

const fs = require('fs'), file = process.argv[2], cont = process.argv[3];
fs.writeFile(file, cont, 'utf8', (err,data) => {
  if (err) {
    console.error(err)
    return
  }
});
