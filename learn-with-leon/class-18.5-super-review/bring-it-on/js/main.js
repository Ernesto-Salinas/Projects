// *Variables*
// Create a variable and console log the value
let var1=22
console.log(var1)
// Create a variable, add 10 to it, and alert the value
var2=23
console.log(var2+10)
// *Functions*
// Create a function that subtracts 4 numbers and alerts the difference
function subFour(num1, num2, num3, num4){
    ans=num1-num2-num3-num4
    console.log(ans)
}
// Create a function that divides one number by another and returns the remainder
function divOneRetRem(num1, num2){
    ans=num1%num2
    return(ans)
}
// *Conditionals*
// Create a function that adds two numbers and if the sum is greater than 50 alert Jumanji
function addTwo(num1, num2){
    if (num1+num2>50) {
        console.log('Jumanji')
    }
}
// Create a function that multiplys three numbers and if the product is divisible by 3 alert ZEBRA
function MultThree(num1, num2, num3){
    if ((num1*num2*num3)%3==0){
        console.log('ZEBRA')
    }
}
//*Loops*
//Create a function that takes in a word and a number. Console log the word x times where x was the number passed in
function random (wd1, num1){
    for (x=0; x<num1;x++){
        console.log(wd1)
    }
}