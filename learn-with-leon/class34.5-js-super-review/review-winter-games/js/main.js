//Create a function that takes in an array of numbers. Return a new array containing every even number from the original array (do not use map or filter)
function checkArray(arr){
    ans=[]
    for (x in arr){
        if ((arr[x])%2===0){
            ans.push(arr[x])
        }
    } return(ans)
}
