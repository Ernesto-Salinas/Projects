/*
Instructions
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

Given Code:
function disemvowel(str) {
  return str;
}
*/

//version 1
function disemvowel(str) {
    ans = ''
    for (char of str){
        if (char == "a" || char == "e" || char == "i" || char == "o" || char == "u" || char == 'A' || char == 'E' || char == 'I' || char == 'O' || char == 'U'){
            continue
        }else{
            ans += char
        }
    }return ans
}

// Tests
console.log(disemvowel("This website is for losers LOL!"))
console.log(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))
console.log(disemvowel("What are you, a communist?"))

//version 2
function disemvowel2(str) {
    return str.replace(/[aeiou]/gi, '')
}

// Tests
console.log(disemvowel2("This website is for losers LOL!"))
console.log(disemvowel2("No offense but,\nYour writing is among the worst I've ever read"))
console.log(disemvowel2("What are you, a communist?"))