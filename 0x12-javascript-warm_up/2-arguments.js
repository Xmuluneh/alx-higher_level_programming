#!/usr/bin/node
const argLen = process.argv.length;
if (argLen === 3) {
  console.log("Argument Found");
} else if (argLen > 3) {
  console.log("Arguments found");
} else {
  console.log("No argument");
}
