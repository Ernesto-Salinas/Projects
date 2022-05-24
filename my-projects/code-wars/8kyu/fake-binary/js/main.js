// Instructions
// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

// Note: input will never be an empty string

function fakeBin(x){
    num=''
    for (i=0; i<x.length; i++){
        if (x.charAt(i)<5){
            num+='0'
        } else{
            num+='1'
        }
    }return(num)
}