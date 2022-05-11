// var countBits = function findBinary(n) {
    // Program Me
function findBinary(n){
    let binary = ''
    while (n>=1){
        bit=n%2
        binary+=bit
        n=Math.floor(n/2)
        console.log(n)
        console.log(binary)
        if (n===1){
            bit=n%2
            binary+=bit
            n-=1
            console.log(n)
            console.log(binary)
        }
    } return (Number(binary))
}


function test (){
    for (let i = 1; i < 5; i++) {
        console.log(i)
    }
}
