//Create a function that has a loop that prints '21' 21 times to the console and then call that function
//Bonus can you make it print '21' 21 times to the dom?
function loop (){
    z=' 21'
    for (let a=0; a<21; a++) {
        console.log(z)
        document.querySelector("#savageSays").innerText += z
    }
}
loop()
