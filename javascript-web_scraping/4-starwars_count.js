#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

let url args = process.argv[2];
let request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let json= JSON.parse(body);
    let results = json['results'];
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      let chars = (results[i]['characters']);
      for (let j = 0; j < chars.length; j++) {
        let check = chars[j].endsWith('18/');
        if (check) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
