#!/usr/bin/node
import { dict } from './101-data';
const myValue = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] ? [...acc[value], key] : [key];
  return acc;
}, {});
console.log(myValue);
