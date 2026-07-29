// Instructions
// Given an array of integers, return a new array with each value doubled.

// For example:
// [1, 2, 3] --> [2, 4, 6]

function maps(x){
    result=[]
    for (let i=0; i<x.length; i++){
        result.push(x[i]*2)
    }return(result)
}