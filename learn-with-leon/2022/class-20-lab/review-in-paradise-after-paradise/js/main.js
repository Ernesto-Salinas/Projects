// Create a function that takes in an array. If the first number, is less than the last number, alert "Hi". If the first number is greater than the last number, alert "Bye". If they are equal, alert "We close in an hour".
function arrayAnalysis(array){
    if(array[0]<array[array.length-1]){
        // alert("Hi")
        console.log("Hi")
    }else if(array[0]>array[array.length-1]){
        // alert("Bye")
        console.log("Bye")
    }else{
        // alert("We close in an hour")
        console.log("We close in an hour")
    }
}