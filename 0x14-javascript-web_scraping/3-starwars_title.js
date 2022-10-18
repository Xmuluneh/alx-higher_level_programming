#!/usr/bin/node
const request = require('request');
const id = Number(process.argv[2]);
request(
  `https://swapi-api.hbtn.io/api/films/${id}`,
  function (error, response, body) {
    if (error) {
      return;
    }
    console.log(JSON.parse(body).title);
  }
);
