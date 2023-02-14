/* splice
How to delete an element from the array?

The arrays are objects, so we can try to use delete: */

let arr = ["I", "go", "home"]

delete arr[1]

console.log(arr)

arr.splice(1,1)

console.log(arr)

// In the next example we remove 3 elements and replace them with the other two:

let arr2 = ["I", "study", "JavaScript", "right", "now"]

arr2.splice(0,3, "Let's", "dance")

console.log(arr2)

// Here we can see that splice returns the array of removed elements:

let arr3 = ["I", "study", "JavaScript", "right", "now"]

let removed = arr3.splice(0,2)

console.log(removed)

// The splice method is also able to insert the elements without any removals. For that we need to set deleteCount to 0:

let arr4 = ["I", "study", "JavaScript"]

arr4.splice(2,0,"complex","language")

console.log(arr4)

/* Negative indexes allowed

Here and in other array methods, negative indexes are allowed. They specify the position from the end of the array, like here: */

let arr5 = [1,2,5]

arr5.splice(-1,0,3,4)

console.log(arr5)

/* slice
The method arr.slice is much simpler than similar-looking arr.splice.

The syntax is:
arr.slice([start], [end]) */

arr6 = ['t','e','s','t']

console.log(arr6.slice(0,1))
console.log(arr6.slice(1,2))
console.log(arr6.slice(0,2))
console.log(arr6.slice(1,3))
console.log(arr6.slice(1,4))
console.log(arr6.slice(-3))
console.log(arr6.slice(-3,4))

/* concat
The method arr.concat creates a new array that includes values from other arrays and additional items.

The syntax is:
arr.concat(arg1, arg2...)

It accepts any number of arguments – either arrays or values.
The result is a new array containing items from arr, then arg1, arg2 etc.
If an argument argN is an array, then all its elements are copied. Otherwise, the argument itself is copied.

For example: */

let arr7 = [1,2]

// create an array from: arr7 and [3,4]
console.log(arr7.concat([3,4]))

// create an array from: arr7 and [3,4] and [5,6]
console.log(arr7.concat([3,4], [5,6]))

// create an array from: arr and [3,4], then add values 5 and 6
console.log(arr7.concat([3,4],5,6))

// Normally, it only copies elements from arrays. Other objects, even if they look like arrays, are added as a whole:

let arrayLike = {
    0: "something",
    length: 1
  };

console.log(arr7.concat(arrayLike))

// …But if an array-like object has a special Symbol.isConcatSpreadable property, then it’s treated as an array by concat: its elements are added instead:

let arrayLike2 = {
    0: "something",
    1: "else",
    [Symbol.isConcatSpreadable]: true,
    length: 2
};

console.log(arr7.concat(arrayLike2))

/* Iterate: forEach

The arr.forEach method allows to run a function for every element of the array.

The syntax:
arr.forEach(function(item, index, array) {
  // ... do something with item
}); */

// For instance, this shows each element of the array:

// for each element call alert:
let arr8=["Bilbo", "Gandalf", "Nazgul"]
// arr8.forEach(alert)


arr8.forEach((item, index, array) => {
  console.log(`${item} is at index ${index} in ${array}`)
})

// Searching in Arrays

// arr.indexOf(item, from) – looks for item starting from index from, and returns the index where it was found, otherwise -1.
// arr.includes(item, from) – looks for item starting from index from, returns true if found.

// Usually these methods are used with only one argument: the item to search. By default, the search is from the beginning.

let arr9 = [1,0, false]

console.log(arr9.indexOf(0))
console.log(arr9.indexOf(false))
console.log(arr9.indexOf(null))

console.log(arr9.includes(1))

// NOTE: Please note that indexOf uses the strict equality === for comparison. So, if we look for false, it finds exactly false and not the zero.

let fruits = ['Apple', 'Orange', 'Apple']

console.log(fruits.indexOf('Apple'))
console.log(fruits.lastIndexOf('Apple'))

/* find and findIndex/findLastIndex

Imagine we have an array of objects. How do we find an object with the specific condition?

Here the arr.find(fn) method comes in handy.

The syntax is:

let result = arr.find(function(item, index, array) {
  // if true is returned, item is returned and iteration is stopped
  // for falsy scenario returns undefined
}); */

let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];

let user = users.find(item => item.id == 1)
console.log(user)
console.log(user.name)

let users2 = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"},
  {id: 4, name: "John"}
];

console.log(users2.findIndex(user => user.name == 'John'))
console.log(users2.findLastIndex(user => user.name == 'John'))

/* filter
The find method looks for a single (first) element that makes the function return true.

If there may be many, we can use arr.filter(fn).

The syntax is similar to find, but filter returns an array of all matching elements:

let results = arr.filter(function(item, index, array) {
  // if true item is pushed to results and the iteration continues
  // returns empty array if nothing found
}); */

let users3 = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];

let someUsers = users3.filter(item => item.id < 3)
console.log(someUsers)
console.log(someUsers.length)

/* Transform an array
Let’s move on to methods that transform and reorder an array.

map
The arr.map method is one of the most useful and often used.

It calls the function for each element of the array and returns the array of results.

The syntax is:

let result = arr.map(function(item, index, array) {
  // returns the new value instead of item
}); */

let lengths = ['Bilbo', 'Gandalf', 'Nazgul'].map(item => item.length)
console.log(lengths)

/* sort(fn)
The call to arr.sort() sorts the array in place, changing its element order.

It also returns the sorted array, but the returned value is usually ignored, as arr itself is modified.

For instance:

let arr = [ 1, 2, 15 ];

// the method reorders the content of arr
arr.sort();

alert( arr ); */

let arr10 = [ 1, 2, 15 ];
console.log(arr10)
arr10.sort()
console.log(arr10)

