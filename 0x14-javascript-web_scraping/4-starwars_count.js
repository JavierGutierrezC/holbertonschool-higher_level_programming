#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    let newList = [];
    const movies = JSON.parse(body).results;
    // console.log(movies);
    for (const x of movies) {
      newList = x.characters;
      // console.log(newList);
      for (const y of newList) {
        if (y.includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
