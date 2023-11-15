#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let fig = 0; fig < this.height; fig++) console.log('X'.repeat(this.width));
  }
};
