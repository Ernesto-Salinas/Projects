//Arrays

//Create and array of tv shows. Loop through and print each show to the console

let tvShows = ['Ren & Stimpy', 'The Jetsons', 'Dragonball Z', 'House M.D.']

tvShows.forEach((x,i) => console.log(x))

//Create and array of numbers

nums = [4,6,5,7,9,4,21,56,88,99,710]

//Return a new array of numbers that includes every even number from the previous Arrays

// Method 1

function findEvens(arr){
    let evenNums=[]
    for (let i=0; i<arr.length;i++){
        if (arr[i]%2===0){
            evenNums.push(arr[i])
        }
    }return evenNums
}


// Method 2 Arrow Function

let evenArrowFunc = arr => arr.filter(n => n%2===0)




//Create a function that takes in an array of numbers
//Alert the sum of the second lowest and the second highest number

function addSecondLowestAndSecondHighest(arr1){
    let sorted = arr1.sort((a,b)=>a-b)
    console.log(sorted[1]+ sorted[sorted.length-2])
}