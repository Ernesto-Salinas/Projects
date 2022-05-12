// Write Number in Expanded Form

// You will be given a number and you will need to return it as a string in Expanded Form. 

// For example:
// expandedForm(12); // Should return '10 + 2'
// expandedForm(42); // Should return '40 + 2'
// expandedForm(70304); // Should return '70000 + 300 + 4'

function expandedForm(num){
    num=String(num)
    let exp=''
    for (let x in num){
        zeros=''
        if(num[x]!=0){
            let i = Number(x)+1
            while (i<num.length){
                zeros+='0'
                i++
            } if (x==0){
                exp=num[x]+zeros
            } else{
                exp+=' + '+num[x]+zeros
            }
        }
    } return(exp)
}