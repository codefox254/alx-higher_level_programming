#!/usr/bin/node
// Define the executeXTimes function
function executeXTimes(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
};