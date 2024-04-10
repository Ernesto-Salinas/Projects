//Create a function that takes in an array of numbers. Multiply each number together and alert the product. 
let numArr = [4,8,12,16]

function multArr(arr){
    let jet = 1
    /* for(let i=0; i < arr.length; i++){
        jet*=arr[i]
    }alert(jet) */
    numArr.forEach(x => jet*=x)
    alert(jet)
}