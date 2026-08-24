/*
Instructions
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

Given Code:
function bmi(weight, height) {
  return "";
}
*/

function bmi(weight, height) {
    bmi_num = weight/(height**2);
    if (bmi_num <= 18.5){
        return "Underweight"
    } if (bmi_num <= 25.0){
        return "Normal"
    } if (bmi_num <= 30.0){
        return "Overweight"
    } if (bmi_num > 30){
        return "Obese"
    }
}

// Tests
console.log(bmi(50, 1.80)) // bmi: 15.4 - "Underweight"
console.log(bmi(80, 1.80)) // bmi: 24.69 - "Normal"
console.log(bmi(90, 1.80)) // bmi: 27.78 - "Overweight"
console.log(bmi(100, 1.80)) // bmi: 30.86 - "Obese"
