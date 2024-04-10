//Create an array of movie titles. Loop through the array and each element to the h2.
movies=['John Wick','John Wick 2','John Wick 3']

for (i=0; i<movies.length; i++){
    document.querySelector('h2').innerText+=movies[i]
}

//Create an array of numbers. Loop through the array and three to each number and replace the old number.
let numArr=[2,4,5,9]
numArr.forEach((x,i)=> {numArr[i]= x+3})

//Find the average of all the numbers from question three
let sumNums=0
// numArr.forEach((x,i)=> {
//     sumNums+=x
//     console.log(sumNums)
//     result=sumNums/numArr.length
//     return(result)
// })

for (let i=0;i<numArr.length; i++){
    sumNums+=numArr[i]
}console.log(sumNums/numArr.length)