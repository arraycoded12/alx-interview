#!/usr/bin/node

/**
 * 0. Star Wars Characters
 *
 * Prints all characters of a Star Wars movie.
 *
 */

const movieId = process.argv[2];
if (process.argv.length !== 3 || !Number(movieId)) {
  process.exit(1);
}

const request = require('request');
const filmUri = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const printCharacterName = (characterUri) => {
  return new Promise((resolve, reject) => {
    request.get(characterUri, (error, response, body) => {
      if (error) {
        console.log('Error: ', error);
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

const main = async () => {
  const charactersUri = await new Promise((resolve, reject) => {
    request.get(filmUri, (error, response, body) => {
      if (error) {
        console.log('Error: ', error);
        reject(error);
      } else {
        resolve(JSON.parse(body).characters);
      }
    });
  });

  for (const characterUri of charactersUri) {
    const name = await printCharacterName(characterUri).catch((error) => {
      console.log(error);
    });
    console.log(name);
  }
};
main();
