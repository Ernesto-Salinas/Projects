// *Variables*
// Declare a variable, reassign it to your fav holiday, make sure it is in all caps, and print the value to the console

let var1 = "leggo"
var1 = "CHRISTMAS"
console.log(var1)

//Declare a variable, assign it a string, alert the last three characters in the string (Use your google-fu and the MDN)

let lance = "JJ Horray"
console.log(lance.slice(-3))

// *Functions*
// Create a function that takes in 5 numbers. Subtract all five from 100. Alert the absolute value of the difference. Call the function.
function goodTry(n1,n2,n3,n4,n5){
    console.log(Math.abs(100-n1-n2-n3-n4-n5))
}

// Create a function that takes in 3 numbers. Console log lowest and highest values. Call the function.

// Method 1
function threeNums(n1,n2,n3){
    lowestVal = n1
    highestVal = n1
    arr=[n1,n2,n3]
    for (let i = 0; i<arr.length; i++){
        if (arr[i]>highestVal){
            highestVal=arr[i]
        }else if (arr[i]<lowestVal){
            lowestVal=arr[i]
        }
    }console.log(`The lowest number is ${lowestVal} and the highest number is ${highestVal}`)
}

threeNums(3,7,6)

// Method 2
function minMax(n1,n2,n3){
    let minAns = Math.min(n1,n2,n3)
    let maxAns = Math.max(n1,n2,n3)
    console.log(`The lowest number is ${minAns} and the highest number is ${maxAns}`)
}

minMax(15,34,19)

// *Conditionals*
//Create a function that returns heads or tails randomly and as fairly as possible. Call the function.

function random(){
    ans = Math.random()
    if (ans<0.5){
        return 'tails'
    }else{
        return 'heads'
    }
}

//*Loops*
//Create a function that takes in a number. Console log the result of heads or tails using the previous function x times where x is the number passed into the function. Call the function.
function imTired(n1){
    for(let i = 1; i <= n1; i++){
        let ans = random()
        console.log(ans)
    }
}