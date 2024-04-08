#!/usr/bin/node
// Define the incr function to increment an integer value
function incr(number) {
    return number + 1;
}

// Define the incrementAndCall function
function incrementAndCall(number, theFunction) {
    const incrementedNumber = incr(number);
    theFunction(incrementedNumber);
}

// Export the incrementAndCall function to make it visible from outside
module.exports = {
    incrementAndCall: incrementAndCall,
    incr: incr
};
