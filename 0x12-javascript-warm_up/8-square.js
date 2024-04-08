#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];
const size = parseInt(arg);
if (!isNaN(size)) {
    for (let i = 0; i < size; i++) {
        const row = 'X'.repeat(size);
        console.log(row);
    }
} else {
    console.log("Missing size");
}
