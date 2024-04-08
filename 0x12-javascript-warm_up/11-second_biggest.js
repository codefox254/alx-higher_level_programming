#!/usr/bin/node
// Get the arguments passed to the script (excluding the first two elements
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
    console.log(0);
} else {
    const integers = args.map(arg => parseInt(arg));
    const sortedIntegers = integers.sort((a, b) => b - a);
    const secondLargest = sortedIntegers[1];
    console.log(secondLargest);
}
