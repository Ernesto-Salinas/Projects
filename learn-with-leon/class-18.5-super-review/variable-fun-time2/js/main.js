//--- Easy
//create a variable and assign it a number
let num = 2

//minus 10 from that number
let min = num-10
//print that number to the console
console.log(min)
//--- Medium
//create a variable that holds a value from the input
let inp = Number(document.querySelector('input').value)
//add 25 to that number
let addToInp = inp + 25
//alert that number
// alert(addToInp)
//--- Hard
//create a variable that holds the h1
let h1Var=document.querySelector('h1')
//add an event listener to that element that console logs the sum of the two previous variables

function addTwoNums(){
    inputNum=document.querySelector('input').value
    document.querySelector('h2').innerText="You have chosen "+inputNum+"!!"
}

h1Var.addEventListener('click',addTwoNums)
