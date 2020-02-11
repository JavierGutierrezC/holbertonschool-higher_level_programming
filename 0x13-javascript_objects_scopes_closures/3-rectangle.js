#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let y;
    for (y = 0; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
