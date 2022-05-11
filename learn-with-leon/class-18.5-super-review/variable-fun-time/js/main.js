//--- Easy
//create a variable and assign it a number
let var1 = 1

//minus 10 from that number
var1-=10
//print that number to the console
console.log(var1)
//--- Medium
//create a variable that holds a value from the input
let numFromInput=document.querySelector('input').value
//add 25 to that number
numFromInput+=25
//alert that number
alert(numFromInput)
//--- Hard
//create a variable that holds the h1
let h1Var=document.querySelector('h1')
//add an event listener to that element that console logs the sum of the two previous variables
h1Var.addEventListener('click', addTwoNums)

function addTwoNums(){
    console.log(var1+Number(numFromInput))
}



h1Var.addEventListener('click',inputResponse)

function inputResponse(){
    numFromInput=document.querySelector('input').value
    document.querySelector('h2').innerText =numFromInput+' for the win!'
}