// Instructions

/* An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case) */

function isIsogram(str){
    let placeHolder=''
    for (i in str){
        if (placeHolder.indexOf(str.charAt(i)) == -1){
            placeHolder += (str.charAt(i).toLowerCase())
            placeHolder += (str.charAt(i).toUpperCase())
            console.log(placeHolder)
        }else{
            return false
        }
    }return true
}

// Test to make an algarithm that can check if each word in a sentence is an isogram

// function areAllWordsInSentenceIsogram(str){
//     let arr = str.split(' ')
//     console.log('array is '+arr)
//     for (let x=0; x < arr.length; x++){
//         console.log('index of array is '+x)
//         console.log('word being iterated is '+arr[x])
//         let placeHolder=''
//         for (i in arr[x]){
//             console.log('index of word is '+i)
//             console.log('character being iterated is '+arr[x].charAt(i))
//             if (placeHolder.indexOf(arr[x].charAt(i)) == -1){
//                 placeHolder += (arr[x].charAt(i).toLowerCase())
//                 placeHolder +=(arr[x].charAt(i).toUpperCase())
//                 console.log('placeholder equals '+placeHolder)
//             }else{
//                 return false
//             }
//         }
//     }return true
// }


// algarithm that can check if each word in a sentence is an isogram

function areAllWordsInSentenceIsogram(str){
    let arr = str.split(' ')
    for (let x=0; x < arr.length; x++){
        let placeHolder=''
        for (i in arr[x]){
            if (placeHolder.indexOf(arr[x].charAt(i)) == -1){
                placeHolder += (arr[x].charAt(i).toLowerCase())
                placeHolder += (arr[x].charAt(i).toUpperCase())
            }else{
                return false
            }
        }
    }return true 
}

console.log(areAllWordsInSentenceIsogram('same chars may not be same case'))