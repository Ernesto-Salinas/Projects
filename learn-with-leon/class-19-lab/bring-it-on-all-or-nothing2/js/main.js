// *Variables*
// Declare a variable, assign it a boolean, and alert the value
let var1 = true
// alert(var1)
console.log(var1)

// Declare a variable, reassign it to your favorite color, and console log the value
let var2 = ''
var2 = 'blue'
console.log(var2)

// *Functions*
// Create a function that takes in 4 numbers and returns the sum of the first 3 numbers divided by the fourth. Return the result. Call the function.
function sum3div(n1,n2,n3,n4){
    sum=(n1+n2+n3)/n4
    return sum
}

// Create a function that takes in 2 numbers. Console log the first number to the power of the second. Call the function.
function exp2(n1,n2){
    ans=Math.pow(n1,n2)
    console.log(ans)
}

// *Conditionals*
// Create a function that takes in a boolean and a string. If the boolean is true, alert the string. If the boolean is false, console log the string
function bool(b1,str){
    // // Note: First Attempt
    // if (b1){
    //     alert(str)
    // }else{
    //     console.log(str)
    // }

    // **NOTE: Same function as above but expessed as a TERNARY
    b1 ? alert(str) : console.log(str)
}

// **NOTE THE function above expressed as a function expression
const bool2 = (b1,str) => b1 ? alert(str) : console.log(str)

//*Loops*
//Create a function that takes in a number. Console log all values from 1 to that number, but if the number is divisible by 3 log "fizz" instead of that number, if the number is divisible by 5 log "buzz" instead of the number, and if the number is divisible by 3 and 5 log "fizzbuzz" instead of that number
function loopitup(n1){
    for (let i = 1; i<=n1; i++){
        if(i%3==0 && i%5==0){
            console.log('fizzbuzz')
        }else if(i%3==0){
            console.log('fizz')
        }else if(i%5==0){
            console.log('buzz')
        }else{
            console.log(i)
        }
    }
}