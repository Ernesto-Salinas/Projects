/*
Instructions:
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

Given Code:
function removeExclamationMarks(s) {
  return '';
}
*/

function removeExclamationMarks(s) {
    return s.replaceAll("!", "")
}

// Tests
console.log(removeExclamationMarks("Hello World!"))