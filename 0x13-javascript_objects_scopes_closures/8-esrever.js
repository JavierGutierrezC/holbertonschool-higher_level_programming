#!/usr/bin/node
exports.esrever = function (list) {
  const reversList = [];
  let x;
  for (x = list.length - 1; x >= 0; x--) {
    reversList.push(list[x]);
  }
  return (reversList);
};
