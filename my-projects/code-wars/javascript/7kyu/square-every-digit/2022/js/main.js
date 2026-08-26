// Instructions

// square every digit of a number and concatenate them.

// For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

// Note: The function accepts an integer and returns an integer

function squareDigits(num){
    result=0
    SquaredNum=0
    numString=num.toString()
    for (let i=0; i<numString.length; i++){
        squaredNum=numString.charAt(i)*numString.charAt(i)
        result+=squaredNum.toString()
    } return(Number(result))
}