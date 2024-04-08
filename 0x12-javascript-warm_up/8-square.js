#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];
// Convert the argument to an integer using parseInt
const size = parseInt(arg);
// Check if the conversion resulted in a valid number
if (!isNaN(size)) {
    // Loop to print each row of the square
    for (let i = 0; i < size; i++) {
        // Create a string with 'X' repeated 'size' times
        const row = 'X'.repeat(size);
        // Print the row
        console.log(row);
    }
} else {
    // Print an error message if the argument couldn't be converted to an integer
    console.log("Missing size");
}
