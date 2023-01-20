//Create an array of movie titles. Loop through the array and each element to the h2.
let movieArr = ["Top Gun", "Top Gun: Maverick", "The Fast & The Furious", "Fast 9"]

movieArr.forEach((x,i)=> document.querySelector("h2").innerText += x+', ')

//Create an array of numbers. Loop through the array and three to each number and replace the old number.
let numArr = [1,2,3,4]
numArr.forEach((x,i) => numArr[i]+=3)
//Find the average of all the numbers from question three
let avg = 0
// function averageArray(){
//     numArr.forEach((x,i)=>{
//         avg += numArr[x]
//         return avg
//     })
//     console.log(avg)
//     ans=avg/numArr.length
//     console.log(ans)
// }

numArr.forEach((x,i)=> avg+=x)
console.log(avg/numArr.length)