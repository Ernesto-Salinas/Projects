// Instructions
// Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

// function pigIt(str){
//     for (i=0; i<str.length; i++){
//         if (str.charAt(i+1))
//     }
// }

function pigIt(str){
    let word=''
    let phrase=''
    for (x in str){
        if(x==str.length-1){
            word+=str[x]
            word=word.slice(1)+word[0]+'ay'
            phrase+=word
            word=''
        }else if (str[x]==' '){
            word=word.slice(1)+word[0]+'ay'
            phrase+=word+" "
            word=''
        }else{
            word+=str[x]
        }
    }return(phrase)
}