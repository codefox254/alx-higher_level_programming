#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];
// Convert the argument to an integer using parseInt
const x = parseInt(arg);

// Check if the conversion resulted in a valid number
if (!isNaN(x)) {
    // Loop x times and print "C is fun" each time
    for (let i = 0; i < x; i++) {
        console.log("C is fun");
    }
} else {
    // Print an error message if the argument couldn't be converted to an integer
    console.log("Missing number of occurrences");
}
