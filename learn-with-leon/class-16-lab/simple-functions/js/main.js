//---Easy
//create a function that subtracts two numbers and alerts the difference
function subtract (n1, n2){
    ans=n1-n2
    alert(ans)
}
//create a function that divides three numbers and console logs the quotient
function divide3(num1,num2,num3){
    ans2=num1/num2/num3
    console.log(ans2)
}
//create a function that multiplys three numbers and returns the product
function mul3(n3,n4,n5){
    ans3=n3*n4*n5
    return(ans3)
}
//---Medium
//create a function that takes in three numbers. Add the first two numbers and return the remainder of dividing the sum of the first two numbers by the third number
function equation(n6,n7,n8){
    ans4=(n6+n7)%n8
    return(ans4)
}
//---Hard
//create a function that takes in 4 numbers. Multiply the first two numbers. 
// If the product is greater than 100 add the sum of the last two numbers and console log the value. 
// If the product is less that 100, subtract the difference of the last two numbers and console log the value. 
// If the product is 100, multiply the first three numbers together and alert the remainder of dividing the fourth number
function equation2(n9,n10,n11,n12){
    ans5=n9*n10
    if(ans5>100){
        ans6=n11+n12
        console.log(ans6)
    }else if(ans5<100){
        ans6=n11-n12
        console.log(ans6)
    }else{
        ans6=n9*n10*n11
        alert(ans6%n12)
    }
}