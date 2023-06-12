#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const todos = JSON.parse(body);
    const dash = {};
    for (let i = 0; i < todos.length; i++) {
      const statuss = (todos[i].completed);
      const key = todos[i].userId.toString();
      if (statuss) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
