/*
Instructions:
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

Given Code:
function fakeBin(x){

}
*/

function fakeBin(x){
    ans = ""
    for (let num of x){
        if(num<5){
            ans += 0
        } else if (num>=5){
            ans += 1
        }
    }return ans
}

// Tests
console.log(fakeBin('45385593107843568')) // '01011110001100111'
console.log(fakeBin('509321967506747')) // '101000111101101'
console.log(fakeBin('366058562030849490134388085')) // '011011110000101010000011011'