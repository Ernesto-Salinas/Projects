//Write your pseduo code first! 
// C to F
document.querySelector('h2').addEventListener('click',tempConv)
function tempConv(){
    Celc=Number(document.querySelector('input').value)
    Fahr=(Celc*(9/5))+32
    document.querySelector('h3').innerText=Celc+" degrees Celcius is equal to "+Fahr+" degrees Fahrenheit."
}