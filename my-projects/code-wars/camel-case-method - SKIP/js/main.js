// Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. 
// All words must have their first letter capitalized without spaces.

// For instance:

// "hello case".camelCase() => HelloCase
// "camel case word".camelCase() => CamelCaseWord

camelCase : function(){
    string=''
    for (let x in this){
        if (this[x]===' '){
        } else if (this[x-1]===' '){
            string+=this[x].toUpperCase()
        } else{
            string+=this[x]
        }
    }return (this)
}