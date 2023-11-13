#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let fig = 0; fig < x; fig++) theFunction();
};
