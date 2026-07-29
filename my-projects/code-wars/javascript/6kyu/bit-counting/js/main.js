// Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

function findBinary(n){
    let binary = ''
    let bitNum=0
    while (n>=1){
        bit=n%2
        binary=bit+binary
        n=Math.floor(n/2)
    } for (let x in binary){
        if (binary[x]==1){
            bitNum+=1
        }
    } return (Number(bitNum))
}