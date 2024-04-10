#!/usr/bin/node
// Import the list from 100-data.js
const { list } = require('./100-data');
const newList = list.map((value, index) => value * index);
console.log('Initial list:', list);
console.log('New list:', newList);
