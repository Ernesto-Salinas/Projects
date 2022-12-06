//Create an array of movies with at least three movies.
let movieArray=['The Fast and the Furious','Top Gun: Maverick','2 Fast 2 Furious','Jurassic World']
//Using the array from above, store the first movie in a variable
let firstMovie=movieArray[0]
//Get the length of the original array and store it in a new variable
let arrLength=movieArray.length
//Get the last element in that array and store it in a new variable. What if your array was really large and you didn't know the last index? Would your solution still work?
lastMovie=movieArray[movieArray.length-1]
console.log(lastMovie)
movieArray[4]='Sonic'
lastMovie=lastMovie=movieArray[movieArray.length-1]
console.log(lastMovie)