#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {

  let reversed_list = [];
  while (list.length > 0) {
    reversed_list.push(list.pop());
  }
  return reversed_list;
};
