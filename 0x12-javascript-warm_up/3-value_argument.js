#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];
if (arg === undefined) {
    console.log('No argument');
} else {
    console.log(arg);
}
