// Instructions
// This time no story, no theory. The examples below show you how to write function accum:

// Examples:
// accum("abcd") -> "A-Bb-Ccc-Dddd"
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
// accum("cwAt") -> "C-Ww-Aaa-Tttt"

// The parameter of accum is a string which includes only letters from a..z and A..Z.

function accum(s) {
    let result=''
    for (let i=1; i<=s.length; i++){
        let count = 0
        while(count<i){
            if(i==1 && count==0){
                result+=s.charAt(i-1).toUpperCase()
                count++
            }else if (count==0){
                result+="-"+s.charAt(i-1).toUpperCase()
                count++
            } else{
                result+=s.charAt(i-1).toLowerCase()
                count++
            }
        }
    }return(result)
}