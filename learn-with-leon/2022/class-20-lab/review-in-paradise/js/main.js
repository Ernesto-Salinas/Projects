// *Variables*
// Declare a variable, reassign it to your favorite food, and alert the value
let var1 = "word"
var1="pizza"

//Declare a variable, assign it a string, alert the second character in the string (Use your google-fu and the MDN)
let var2 = "string"
// alert(var2[1])
console.log(var2[1])

// *Functions*
// Create a function that takes in 3 numbers. Divide the first two numbers and multiply the last. Alert the product. Call the function.
function div2AndMul(n1,n2,n3){
    ans=(n1/n2)*n3
    // alert(ans)
    console.log(ans)
}
div2AndMul(12,3,2)

// Create a function that takes in 1 number. Console log the cube root of the number. Call the function.
function cubeRoot(n1){
    console.log(Math.cbrt(n1).toFixed(4))
}

// *Conditionals*
//Create a function that takes in a month. If it is a summer month alert "YAY". If another other month, alert "Booo"
function summerBest(month){
    month=month.toLowerCase()
    if(month==="june" || month==="july" || month==="august" || month==="september"){
        console.log("YAY")
    }else{
        console.log("Booo")
    }
}

//*Loops*
//Create a function that takes in a number. Console log every number from 1 to that number while skipping multiples of 5.
function loopDeLoop(n1){
    for (let i =1; i<=n1;i++){
        if(i%5!==0){
            console.log(i)
        }
    }
}