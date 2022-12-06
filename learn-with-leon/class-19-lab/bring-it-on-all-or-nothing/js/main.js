// *Variables*
// Declare a variable, assign it a boolean, and alert the value
let var1=true
// alert(var1)
console.log(var1)

// Declare a variable, reassign it to your favorite color, and console log the value
let var2='blue'
var2='red'
console.log(var2)

// *Functions*
// Create a function that takes in 4 numbers and returns the sum of the first 3 numbers divided by the fourth. Return the result. Call the function.
function sumFourNums(n1,n2,n3,n4){
    sumDiv=(n1+n2+n3)/n4
    return(sumDiv)
}

console.log(sumFourNums(1,2,3,4))

// Create a function that takes in 2 numbers. Console log the first number to the power of the second. Call the function.
function powerTwo(n1,n2){
    result=n1
    let count = 1
    while(count < n2){
        result*=n1
        count++
    } console.log(result)
}

console.log(powerTwo(2,4))

// *Conditionals*
// Create a function that takes in a boolean and a string. If the boolean is true, alert the string. If the boolean is false, console log the string
function whoKnows(bool,string){
    if( bool){
        alert(string)
    }else{
        console.log(string)
    }
}
//*Loops*
//Create a function that takes in a number. Console log all values from 1 to that number, but:
// If the number is divisible by 3 log "fizz" instead of that number. 
// If the number is divisible by 5 log "buzz" instead of the number. 
// If the number is divisible by 3 and 5 log "fizzbuzz" instead of that number
function loopNConc(n1){
    result=''
    for(i=1; i<=n1; i++){
        if(i%3===0 && i%5===0){
            console.log('fizzbuzz')
        }else if (i%3===0){
            console.log('fizz')
        }else if(i%5===0){
            console.log('buzz')
        }else{
            console.log(i)
        }
    }
}