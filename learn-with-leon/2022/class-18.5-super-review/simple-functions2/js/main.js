//---Easy
//create a function that subtracts two numbers and alerts the difference
function sub2(num1, num2){
    ans=num1-num2
    // alert(ans)
    console.log(ans)
}
//create a function that divides three numbers and console logs the quotient
function div3(num1,num2,num3){
    let ans=num1/num2/num3
    console.log(ans)
}
//create a function that multiplys three numbers and returns the product
function mul3(num1,num2,num3){
    ans=num1*num2*num3
    return ans
}
//---Medium
//create a function that takes in three numbers. Add the first two numbers and return the remainder of dividing the sum of the first two numbers by the third number
function meddiff(num1, num2, num3){
    let sum=num1+num2
    let div=sum%num3
    return div
}
//---Hard
//create a function that takes in 4 numbers. Multiply the first two numbers. If the product is greater than 100 add the sum of the last two numbers and console log the value. If the product is less that 100, subtract the difference of the last two numbers and console log the value. If the product is 100, multiply the first three numbers together and alert the remainder of dividing the fourth number
function harddiff(num1,num2,num3,num4){
    let mul=num1*num2
    if (mul>100){
        let ans=num3+num4
        console.log(ans)
    }else if (mul<100){
        let ans=num3-num4
        console.log(ans)
    }else{
        mul=num1*num2*num3
        ans=mul%num4
        // alert(ans)
        console.log(ans)
    }
}
