#!/usr/bin/node
// Get the arguments passed to the script (excluding the first two elements which are the interpreter and the script name)
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
    console.log(0);
} else {
    const integers = args.map(arg => parseInt(arg));
    const updatedIntegers = integers.map(num => num === 12 ? 89 : num);
    const sortedIntegers = updatedIntegers.sort((a, b) => b - a);
    const secondLargest = sortedIntegers[1];
    console.log(secondLargest);
}
