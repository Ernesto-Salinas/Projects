// *Variables*
// Create a variable and console log the value
let var1=4
console.log(var1)
// Create a variable, add 10 to it, and alert the value
let var2=5
var2+=10
alert(var2)
// *Functions*
// Create a function that subtracts 4 numbers and alerts the difference
function subFour(num1, num2, num3, num4){
    ans=num1-num2-num3-num4
    alert(ans)
}
// Create a function that divides one number by another and returns the remainder
function divideNum (num1, num2){
    ans=num1%num2
    return(ans)
}
// *Conditionals*
// Create a function that adds two numbers and if the sum is greater than 50 alert Jumanji
function addTwoNums (num1, num2){
    if(num1+num2>50){
        alert("Jumanji!")
    }
}
// Create a function that multiplys three numbers and if the product is divisible by 3 alert ZEBRA
function MulThree(n1,n2,n3){
    let ans=n1*n2*n3
    if (ans%3===0){
        alert('ZEBRA')
    }
}
//*Loops*
//Create a function that takes in a word and a number. 
// Console log the word x times where x was the number passed in
function LoopWordNum (w1,n1){
    for (n=0; n<n1; n++){
        console.log(w1)
    }
}
