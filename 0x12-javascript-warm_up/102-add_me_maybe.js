#!/usr/bin/node
// Define the incrementAndCall function
function incrementAndCall(number, theFunction) {
    const incrementedNumber = number + 1;
    theFunction(incrementedNumber);
};

// Define the addMeMaybe function
function addMeMaybe(number, callback) {
    console.log("New value:", number);
}

// Usage examples
incrementAndCall(5, addMeMaybe); // Correct output: New value: 6
incrementAndCall(5, addMeMaybe); // Correct output: New value: 6
incrementAndCall(-2, addMeMaybe); // Correct output: New value: -1
