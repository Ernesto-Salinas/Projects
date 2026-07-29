// Instructions

// A pangram is a sentence that contains every single letter of the alphabet at least once. 
// For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. 
// Return True if it is, False if not. Ignore numbers and punctuation.

function isPangram(string){
    alphaCheck=true
    if (string.indexOf('a')===-1 || string.indexOf('b')===-1 || string.indexOf('c')===-1 || string.indexOf('d')===-1 || string.indexOf('e')===-1 || string.indexOf('f')===-1 || string.indexOf('g')===-1 || string.indexOf('h')===-1 || string.indexOf('i')===-1 || string.indexOf('j')===-1 || string.indexOf('k')===-1 || string.indexOf('l')===-1 || string.indexOf('m')===-1 || string.indexOf('n')===-1 || string.indexOf('o')===-1 || string.indexOf('p')===-1 || string.indexOf('q')===-1 || string.indexOf('r')===-1 || string.indexOf('s')===-1 || string.indexOf('t')===-1 || string.indexOf('u')===-1 || string.indexOf('v')===-1 || string.indexOf('w')===-1 || string.indexOf('x')===-1 || string.indexOf('y')===-1 || string.indexOf('z')===-1){
        alphaCheck=false
    }return(alphaCheck)
}