#!/usr/bin/node
// Define the function nbOccurrences
exports.nbOccurences = function(list, searchElement) {
    // Initialize a counter variable
    let count = 0;
    for (let i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
            count++;
        }
    }
    return count;
};
