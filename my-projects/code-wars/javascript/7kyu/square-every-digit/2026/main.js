/*
Instructions:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!

Given Code:
function squareDigits(num){
  return 0;
}
*/

function squareDigits(num){
    let numstr = String(num)
    ans = ''
  for (digit of numstr){
    ans += (parseInt(digit)**2)
  }return parseInt(ans)
}

// Tests

// This function prints the square of each digit in num
function TestSquareDigits(num){
    let numstr = String(num)
  for (digit of numstr){
    console.log(parseInt(digit)**2)
  }
}

TestSquareDigits(3212)
console.log(squareDigits(3212))

TestSquareDigits(2112)
console.log(squareDigits(2112))