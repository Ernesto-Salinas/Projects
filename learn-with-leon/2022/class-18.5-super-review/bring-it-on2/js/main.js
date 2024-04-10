// *Variables*
// Create a variable and console log the value
let x = 2
console.log(x)
// Create a variable, add 10 to it, and alert the value
x+=10
// alert(x)
// *Functions*
// Create a function that subtracts 4 numbers and alerts the difference
function sub4(num1,num2,num3,num4){
    let ans=num1-num2-num3-num4
    // alert(ans)
    return ans
}
// Create a function that divides one number by another and returns the remainder
function divR(num1,num2){
    let ans=num1%num2
    return ans
}
// *Conditionals*
// Create a function that adds two numbers and if the sum is greater than 50 alert Jumanji
function con1(num1,num2){
    let ans=num1+num2
    if(ans>50){
        alert('Jumanji')
    }
}
// Create a function that multiplys three numbers and if the product is divisible by 3 alert ZEBRA
function mul3(n1,n2,n3){
    let ans=(n1*n2*n3)%3
    if (ans==0){
        alert("Zebra")
    }
}
//*Loops*
//Create a function that takes in a word and a number. Console log the word x times where x was the number passed in
function alert1(w1,n1){
    for (let i=1; i<=n1;i++){
        console.log(w1)
    }
}