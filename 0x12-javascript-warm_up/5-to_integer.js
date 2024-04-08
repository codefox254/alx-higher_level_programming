#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt
const number = parseInt(arg);

// Check if the conversion resulted in a valid number
if (!isNaN(number)) {
    console.log(`My number: ${number}`);
} else {
    console.log("Not a number");
}
