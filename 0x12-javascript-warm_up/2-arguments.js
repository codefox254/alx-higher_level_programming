#!/usr/bin/node
// Get the arguments passed to the script
const args = process.argv.slice(2);

// Check the number of arguments and print the message accordingly
if (args.length === 0) {
    console.log("No argument");
} else if (args.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
