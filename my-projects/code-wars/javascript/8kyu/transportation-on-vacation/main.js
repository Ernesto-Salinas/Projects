/*
Instructions
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).

Given Code:
function rentalCarCost(d) {
  // Your solution here
}
*/

function rentalCarCost(d) {
    ans = 40*d;
    if (d>=7){
        return ans-50;
    } else if (d>=3){
        return ans-20;
    } else{
        return ans;
    }
}

// Tests
console.log(rentalCarCost(0)) // should be 0
console.log(rentalCarCost(4)) // Should be 140
console.log(rentalCarCost(7)) // Should be 230
console.log(rentalCarCost(10)) // Should be 350