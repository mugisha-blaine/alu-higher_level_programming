#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const reverse_lst = [];
  while (list.length > 0) {
    reverse_lst.push(list.pop());
  }
  return reverse_lst;
};
