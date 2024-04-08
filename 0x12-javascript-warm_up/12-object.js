#!/usr/bin/node
// Get the arguments passed to the script (excluding the first two elements which are the interpreter and the script name)
const args = process.argv.slice(2);

// If no arguments are passed or only one argument is passed, print 0
if (args.length === 0 || args.length === 1) {
    console.log(0);
} else {
    // Convert all arguments to integers
    const integers = args.map(arg => parseInt(arg));

    // Replace 12 with 89
    const updatedIntegers = integers.map(num => num === 12 ? 89 : num);

    // Sort the updated integers in descending order
    const sortedIntegers = updatedIntegers.sort((a, b) => b - a);

    // Find the second largest integer
    const secondLargest = sortedIntegers[1];

    // Print the second largest integer
    console.log(secondLargest);
}
