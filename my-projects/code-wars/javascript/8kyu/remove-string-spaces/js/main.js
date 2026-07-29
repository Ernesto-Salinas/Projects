// Instructions:
// Simple, remove the spaces from the string, then return the resultant string.

function noSpace(x){
    ans=''
    for (let i in x){
        if (x[i]!==' '){
            ans+=x[i]
        }
    }return(ans)
}