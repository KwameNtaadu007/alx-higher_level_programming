#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let fig = 0; fig < this.height; fig++) console.log(c.repeat(this.width));
    }
  }
};
