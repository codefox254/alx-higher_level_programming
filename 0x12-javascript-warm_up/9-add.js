#!/usr/bin/node
// Define the add function with prototype function add(a, b)
function add(a, b) {
    return a + b;
}

// Get the first and second arguments passed to the script
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Check if the arguments can be converted to integers
if (!isNaN(arg1) && !isNaN(arg2)) {
    // Call the add function and print the result
    console.log(add(arg1, arg2));
} else {
    // Print an error message if the arguments couldn't be converted to integers
    console.log("Invalid input. Please provide two integers as arguments.");
}
