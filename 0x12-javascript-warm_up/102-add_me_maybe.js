#!/usr/bin/node

module.exports = {
  addMeMaybe: function (number, funct) {
    funct(number + 1);
  }
};
