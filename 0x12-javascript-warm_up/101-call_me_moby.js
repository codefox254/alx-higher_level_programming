#!/usr/bin/node
// Define the executeXTimes function
function executeXTimes(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
};
function callMeMoby() {
    console.log("Where I am!");
}
executeXTimes(5, callMeMoby); 
executeXTimes(1, callMeMoby); 
executeXTimes(-5, callMeMoby); 
