#!/usr/bin/node
// Define the incrementAndCall function
function incrementAndCall(number, theFunction) {
    const incrementedNumber = number + 1;
    theFunction(incrementedNumber);
}

// Export the incrementAndCall function to make it visible from outside
module.exports.incrementAndCall = incrementAndCall;
