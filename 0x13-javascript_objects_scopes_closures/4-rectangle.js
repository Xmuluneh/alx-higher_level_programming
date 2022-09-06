#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      module.exports = Rectangle;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let recShape = '';
    for (let i = 0; i < this.height; i++) {
      for (let k = 0; k < this.width; k++) {
        recShape += 'X';
      }
      if (i !== this.height - 1) {
        recShape += '\n';
      }
    }
    console.log(recShape);
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}
module.exports = Rectangle;
