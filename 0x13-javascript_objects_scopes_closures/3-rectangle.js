#!/opt/homebrew/bin/node
class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) {
      module.exports = Rectangle;
    }
    this.width = w;
    this.height = h;
  }

  print (params) {
    let recPrint = '';
    for (let i = 0; i < this.height; i++) {
      for (let k = 0; k < this.width; k++) {
        recPrint += 'X';
      }
      if (i !== this.height - 1) {
        recPrint += '\n';
      }
    }
    console.log(recPrint);
  }
}
module.exports = Rectangle;
