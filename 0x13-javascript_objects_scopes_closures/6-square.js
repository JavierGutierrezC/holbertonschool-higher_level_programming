#!/usr/bin/node
const Cuadrado = require('./5-square');

class Square extends Cuadrado {
  charPrint (y) {
    if (y == null) {
      y = 'X';
    }
    for (let z = 0; z < this.width; z++) {
      console.log(y.repeat(this.height));
    }
  }
}

module.exports = Square;
