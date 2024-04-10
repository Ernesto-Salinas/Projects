//Write your pseduo code first! 
// When someone clicks enter while mouse is in the field or clicks on the "convert" button, do the following:
// Check for for value.
document.querySelector('#check').addEventListener('click', convert)
// document.querySelector('#temp').addEventListener('keypress', convert)


function convert() {

    const temp = document.querySelector('#temp').value
  
    // convert number from Celcius to Fahrenheit
    fahr = temp*1.8+32
    
    // respond with answer "# degrees Celcius is equal to # degrees Fahrenheit"
    document.querySelector('#placeToSee').innerText = (temp+" degrees Celcius is equal to "+ parseInt(fahr) +" degrees Fahrenheit")   
  }