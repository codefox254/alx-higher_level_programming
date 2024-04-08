#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];
const x = parseInt(arg);
if (!isNaN(x)) {
    for (let i = 0; i < x; i++) {
        console.log("C is fun");
    }
} else {
    console.log("Missing number of occurrences");
}
