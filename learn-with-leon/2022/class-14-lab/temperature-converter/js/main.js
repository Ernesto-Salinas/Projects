//Write your pseduo code first! 
// user enters temperature needs to be entered into the field
// user clicks on the "Convert" button
// algorithm is run that converts the temperature from Celcius to Fahrenheit
document.querySelector("#convert").addEventListener('click', convert)

function convert(){
    const temp = document.querySelector('#temp').value

    fahr = temp*1.8+32

    // document.querySelector('#ftemp').innerText = temp +" degrees Celcius is equal to "+ fahr +" degrees fahrenheit"
    document.querySelector('#ftemp').innerText = `${temp} degrees Celcius is equal to ${fahr} degrees fahrenheit`
}