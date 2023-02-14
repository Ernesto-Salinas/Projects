// Iterating over an array

const movies = ["The Wolf of Wall Street", "Zootopia", "Babysitting"]

for (const movie of movies){
    console.log(movie)
}

// Updating an array's content
movies.push("Ghostbusters")
console.log(movies[3])

// Removing an element from an array
movies.pop()

console.log(movies)

movies.splice(0,1)

console.log(movies)

/* Musketeers

Write a program that:
- Creates an array named musketeers containing values "Athos", "Porthos" and "Aramis".
- Shows each array element using a "for" loop.
- Adds the "D'Artagnan" value to the array.
- Shows each array element using the forEach() method.
- Remove poor Aramis.
- Shows each array element using a for-of loop. */

let musketeers = ["Athos", "Porthos", "Aramis"]

for (i=0; i<musketeers.length;i++){
    console.log(musketeers[i])
}

musketeers.push("D'Artagnan")

musketeers.forEach(e => console.log(e))

musketeers.splice(2,1)

for (const element of musketeers){
    console.log(element)
}

/* Sum of values

Write a program that creates the following array, then calculates and shows the sum of its values (42 in that case). 
const values = [3, 11, 7, 2, 9, 10] */

const values = [3,11,7,2,9,10]
let sum=0
for (i=0;i<values.length; i++){
    sum+=values[i]
} console.log(sum)

/* List of words

Write a program that asks the user for a word until the user types "stop". The program then shows each of these words, except "stop". */

list = []
function track(word){
    wordlc=word.toLowerCase()
    if (wordlc!=="stop"){
        list.push(word)
    }else{
        finalList=''
        for (i=0;i<list.length;i++){
            finalList+=list[i]+" "
        }console.log(finalList)
    }
}