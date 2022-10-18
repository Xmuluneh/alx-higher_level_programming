#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let x = {};
  const usersIdSet = new Set();
  const todos = JSON.parse(body);
  for (const user of todos) {
    usersIdSet.add(user.userId);
  }
  const userIdArray = Array.from(usersIdSet);
  for (let i = 0; i < userIdArray.length; i++) {
    let complete = 0;
    for (const todo of todos) {
      if (userIdArray[i] === todo.userId) {
        if (todo.completed === true) {
          complete++;
        }
      }
    }
    if (complete === 0) {
      x = {};
    } else {
      x[userIdArray[i]] = complete;
    }
  }
  console.log(x);
});
