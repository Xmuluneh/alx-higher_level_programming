#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) {
      module.exports = Rectangle;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
