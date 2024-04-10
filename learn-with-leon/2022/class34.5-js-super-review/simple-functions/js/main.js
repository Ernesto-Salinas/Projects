//---Easy
//create a function that subtracts two numbers and alerts the difference
function subTwo(n1,n2){
    ans=n1-n2
    // alert(ans)
    return(ans)
}
//create a function that divides three numbers and console logs the quotient
function divThree(n1,n2,n3){
    ans=n1/n2/n3
    console.log(ans)
}
//create a function that multiplys three numbers and returns the product
function mulThree(n1,n2,n3){
    ans=n1*n2*n3
    return(ans)
}
//---Medium
//create a function that takes in three numbers. Add the first two numbers and return the remainder of dividing the sum of the first two numbers by the third number
function addDiv(n1,n2,n3){
    ans1=n1+n2
    ans2=ans1%n3
    return(ans2)
}
//---Hard
//create a function that takes in 4 numbers. 
// Multiply the first two numbers. 
// If the product is greater than 100 add the sum of the last two numbers and console log the value. 
// If the product is less that 100, subtract the difference of the last two numbers and console log the value. 
// If the product is 100, multiply the first three numbers together and alert the remainder of dividing the fourth number
function multFour(n1,n2,n3,n4){
    prod=n1*n2
    if(prod>100){
        sum=n3+n4
        console.log(sum)
    }else if (prod<100){
        diff=n3-n4
        console.log(diff)
    }else {
        prod2=n1*n2*n3
        ans=prod2%n4
        // alert(ans)
        return(ans)
    }
}