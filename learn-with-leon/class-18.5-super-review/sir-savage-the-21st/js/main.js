//Create a function that has a loop that prints '21' 21 times to the console and then call that function
//Bonus can you make it print '21' 21 times to the dom?
function print21 (){
    for (savage=0; savage<21; savage++) {
        document.querySelector('h2').innerText += " 21"
    }
}
print21()