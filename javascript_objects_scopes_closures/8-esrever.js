#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const reverseLst = [];
  while (list.length > 0) {
    reverseLst.push(list.pop());
  }
  return reverseLst;
};
