#!/usr/bin/node
// Define the Rectangle class
class Rectangle {
    // Constructor with w and h parameters
    constructor(w, h) {
        if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
            // If so, create an empty object
            return {};
        }
        this.width = w;
        this.height = h;
    }
}
module.exports = Rectangle;
