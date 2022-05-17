String.prototype.camelCase=function(){
    let result=''
    let z=''
    if (this!=''){
        z=this[0].toUpperCase()+this.slice(1)
    }for (let i=0; i < z.length; i++){
        if(z.charAt(i-1)==' '){
            result+=z.charAt(i).toUpperCase()
        }else if(z.charAt(i)!==' '){
            result+=z.charAt(i)
        }
    }z=''
    return(result)
}