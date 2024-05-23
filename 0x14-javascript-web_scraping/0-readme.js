#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
if (error) {
    console.error('Error reading the file:', error);
  } else {
    // If the file is read successfully, the 'content' parameter will contain the contents of the file as a string.
    console.log(content);
  }
});
