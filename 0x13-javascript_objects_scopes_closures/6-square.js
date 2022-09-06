#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    let letPrint = '';
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let k = 0; k < this.width; k++) {
          letPrint += 'X';
        }
        if (i !== this.height - 1) {
          letPrint += '\n';
        }
      }
      console.log(letPrint);
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let k = 0; k < this.width; k++) {
          letPrint += c;
        }
        if (i !== this.height - 1) {
          letPrint += '\n';
        }
      }
      console.log(letPrint);
    }
  }
}
module.exports = Square;
