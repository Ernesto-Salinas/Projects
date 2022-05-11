//---Easy
//create a function that subtracts two numbers and alerts the difference
function subTwoNums (n1,n2){
    ans=n1+n2
    console.log(ans)
}

//create a function that divides three numbers and console logs the quotient
function divThreeNums(n1,n2,n3){
    ans=n1/n2/n3
    console.log(ans)
}

//create a function that multiplys three numbers and returns the product
function multThreeNums(n1,n2,n3){
    ans=n1*n2*n3
    return(ans)
}
//---Medium
//create a function that takes in three numbers. Add the first two numbers and return the remainder of dividing the sum of the first two numbers by the third number
function addTwoDiv(n1,n2,n3){
    ans=(n1+n2)%n3
    console.log(ans)
}
//---Hard
//create a function that takes in 4 numbers. Multiply the first two numbers. If the product is greater than 100 add the sum of the last two numbers and console log the value. 
// If the product is less that 100, subtract the difference of the last two numbers and console log the value. If the product is 100, multiply the first three numbers together and alert the remainder of dividing the fourth number
function MultTwoThen(n1,n2,n3,n4){
    ans1=n1*n2
    if (ans1>100){
        ans2=n3+n4
        console.log(ans2)
    } else if (ans1<100){
        ans2=n3-n4
        console.log(ans2)
    } else {
        ans2=(n1*n2*n3)%n4
        console.log(ans2)
    }
}