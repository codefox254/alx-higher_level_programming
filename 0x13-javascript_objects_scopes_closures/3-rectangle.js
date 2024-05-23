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
    print() {
        if (!this.width || !this.height) {
            return;
        }
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }
}

// Export the Rectangle class to make it accessible from outside the module
module.exports = Rectangle;
