//Write your pseduo code first! 
// Convert temperature from Celcius to Fahrenheit:
// Record Input
// Multiply Input by 9/5 (1.8)
// add 32 to the product
// print the result

document.querySelector('h2').addEventListener('click', convert)
function convert(){
    Cel=document.querySelector('input').value
    Fahr=(Cel*1.8)+32
    document.querySelector('p').innerText=Cel+" degrees Celcius is equal to "+Fahr+" degrees Fahrenheit"
}