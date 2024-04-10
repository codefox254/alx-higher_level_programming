#!/usr/bin/node
// Import the Square class from 5-square.js
const Square5 = require('./5-square');
class Square extends Square5 {
    constructor(size) {
        super(size);
    }
    charPrint(c) {
        // If c is undefined, use the character 'X'
        if (c === undefined) {
            c = 'X';
        }
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
}
module.exports = Square;
