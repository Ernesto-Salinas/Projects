// *Variables*
// Create a variable and console log the value
var1=5
console.log(var1)
// Create a variable, add 10 to it, and alert the value
var2=5
var2+=10
// alert(var2)
console.log(var2)
// *Functions*
// Create a function that subtracts 4 numbers and alerts the difference
function subFour(n1,n2,n3,n4){
    ans=n1-n2-n3-n4
    // alert(ans)
    return(ans)
}
// Create a function that divides one number by another and returns the remainder
function divNums(n1,n2){
    ans=n1%n2
    return(ans)
}
// *Conditionals*
// Create a function that adds two numbers and if the sum is greater than 50 alert Jumanji
function addIfGreaterThan50(n1,n2){
    if(n1+n2>50){
        return('Jumanji')
    }
}
// Create a function that multiplys three numbers and if the product is divisible by 3 alert ZEBRA
function mulThree(n1,n2,n3){
    prod=n1*n2*n3
    if(prod%3==0){
        // alert('ZEBRA')
        return('ZEBRA')
    }
}
//*Loops*
//Create a function that takes in a word and a number. Console log the word x times where x was the number passed in
function loopee(word, num){
    for (i=0; i<num; i++){
        console.log(word)
    }
}