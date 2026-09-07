/*
Instructions:
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]

Given Code:
function digitize(n) {
  //code here
}
*/

function digitize(n) {
    strNum = n.toString()
    strArr = strNum.split("")
    orderedArr = []
    for (element of strArr){
        orderedArr.unshift(parseInt(element))
    } return orderedArr
}

// Tests
console.log(digitize(35231))
console.log(digitize(0))