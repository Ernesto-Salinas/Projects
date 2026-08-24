/*
Instructions:
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5

Given code:
function litres(time) {
  return 0;
}
*/

function litres(time) {
  return Math.floor(time*0.5);
}

// Tests
console.log(litres(0)) // Should be 0
console.log(litres(1)) // Should be 0
console.log(litres(2)) // should be 1
console.log(litres(3)) // Should be 1
console.log(litres(4)) // Should be 2