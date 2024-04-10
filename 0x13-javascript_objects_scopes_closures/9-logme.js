#!/usr/bin/node
// Define a counter variable to keep track of the number of arguments already printed
let count = 0;
exports.logMe = function(item) {
    console.log(`${count}: ${item}`);
    count++;
};
