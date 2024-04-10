#!/usr/bin/node
const fs = require('fs');
// Ensure proper usage
if (process.argv.length !== 5) {
    console.log('Usage: node concat-files.js <source_file1> <source_file2> <destination>');
    process.exit(1);
}
const [, , sourceFile1, sourceFile2, destination] = process.argv;
fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
    if (err1) {
        console.error(`Error reading ${sourceFile1}: ${err1.message}`);
        process.exit(1);
    }
    fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
        if (err2) {
            console.error(`Error reading ${sourceFile2}: ${err2.message}`);
            process.exit(1);
        }
        const concatenatedData = data1 + data2;
        fs.writeFile(destination, concatenatedData, (err) => {
            if (err) {
                console.error(`Error writing to ${destination}: ${err.message}`);
                process.exit(1);
            }
            console.log(`Concatenated files successfully written to ${destination}`);
        });
    });
});
