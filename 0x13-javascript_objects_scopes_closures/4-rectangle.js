#!/usr/bin/node
// Define the Rectangle class
class Rectangle {
    // Constructor with w and h parameters
    constructor(w, h) {
        // Check if w or h is not a positive integer or equal to 0
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
    rotate() {
        // Exchange the values of width and height
        [this.width, this.height] = [this.height, this.width];
    }
    double() {
        // Double the width and height
        this.width *= 2;
        this.height *= 2;
    }
}
module.exports = Rectangle;
