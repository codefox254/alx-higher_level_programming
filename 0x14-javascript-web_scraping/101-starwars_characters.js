#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const util = require('util');
const requestGet = util.promisify(request.get);
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function printCharacters() {
  try {
    const response = await requestGet(url);
    const content = JSON.parse(response.body);
    const characters = content.characters;
    for (const character of characters) {
      const charResponse = await requestGet(character);
      const charContent = JSON.parse(charResponse.body);
      console.log(charContent.name);
    }
  } catch (error) {
    console.error(error);
  }
}

printCharacters();

