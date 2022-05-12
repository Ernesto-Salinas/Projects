// Complete the solution so that it splits the string into pairs of two characters. 
// If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

// Examples:
// * 'abc' =>  ['ab', 'c_']

function splitStrings(str){
    let y = ''
    const list = []
    for(let x in str){
        y+=(str[x])
        if (y.length===2){
            list.push(y)
            y=''
        } else if (Number(x)+1==str.length){
            list.push(y+'_')
            y=''
            return(list)
        }
    } return(list)
}

function test(str){
    for(let x in str){
        if(Number(x)+1==str.length){
            console.log('true')
            console.log(str[x])
            console.log(Number(x)+1)
            console.log(str.length)
            return('end')
        }else
            console.log('false')
            console.log(str[x])
            console.log(Number(x)+1)
            console.log(str.length)
    }
}