#!/usr/bin/node
// Define the factorial function
function factorial(n) {
    // Base case: if n is NaN or less than 0, return 1
    if (isNaN(n) || n < 0) {
        return 1;
    }
    // Base case: if n is 0, return 1
    if (n === 0) {
        return 1;
    }
    // Recursive case: compute factorial using recursion
    return n * factorial(n - 1);
}

// Get the first argument passed to the script
const arg = parseInt(process.argv[2]);

// Compute the factorial and print the result
console.log(factorial(arg));
