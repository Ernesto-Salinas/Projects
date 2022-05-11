//Create a conditonal that checks their age
//If under 16, tell them they can not drive
document.querySelector("h1").addEventListener("click",checkAge)

function checkAge(age){
    age = document.querySelector("#danceDanceRevolution").value
    if(age<16) {
        para.textContent="Sorry! You can't drive :("
    }else if(age<18){
        para.textContent="You can't hate from outside the club, cause you can't even get in! LOL"
    }else if(age<21){
        para.textContent="Sorry bro, you can't drink :P"
    }else if(age<25){
        para.textContent="Nope, you can't rent a car affordably. $$$"
    }else if(age<30){
        para.textContent="You can't rent fancy cars affordably *shrug*"
    }else{
        // document.querySelector("p").value("There's nothing left to look forward to :///")
        para.textContent="There's nothing left to look forward to :///"
    }
}
//If under 18, tell them they can't hate from outside the club, because they can't even get in
//If under 21, tell them they can not drink
//If under 25, tell them they can not rent cars affordably
//If under 30, tell them they can not rent fancy cars affordably
//If under over 30, tell them there is nothing left to look forward too


//--- Harder
//On click of the h1
//Take the value from the input
//Place the result of the conditional in the paragraph
