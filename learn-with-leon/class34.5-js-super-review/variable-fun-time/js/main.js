//--- Easy
//create a variable and assign it a number
let var1=5
//minus 10 from that number
var1-=10
//print that number to the console
console.log(var1)
//--- Medium
//create a variable that holds a value from the input
var2=document.querySelector('input').value
//add 25 to that number
var2+=25
//alert that number
// alert(var2)
console.log(var2)
//--- Hard
//create a variable that holds the h1
let h1Holder=document.querySelector('h1')
//add an event listener to that element that console logs the sum of the two previous variables
document.querySelector('h1').addEventListener('click', sumTwo)

function sumTwo(){
    var2=document.querySelector('input').value
    ans=var1+Number(var2)
    console.log(ans)
}