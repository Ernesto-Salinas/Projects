//Write your pseduo code first! 
// C to F
// when user enters the temperature in Celcius & clicks on "convert":

document.querySelector('h1').addEventListener('click', tempConvert)
// multiply the input value by 1.8 and add 32
// reply "x" degrees in C is equal to "y" degrees in F
function tempConvert(){
    celc=document.querySelector('input').value
    fahr=(celc*1.8)+32
    document.querySelector('p').innerText = celc+" degrees Celcius is equal to "+fahr+" degrees Fahrenheit."
}