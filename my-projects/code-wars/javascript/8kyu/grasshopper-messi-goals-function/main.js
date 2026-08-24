/*
Instructions:
Messi goals function
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

5, 10, 2  -->  17

Given Code:
function goals (laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  // code goes here
}
*/

function goals (laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
    return (laLigaGoals+copaDelReyGoals+championsLeagueGoals)
}

// Tests
console.log(goals (5, 10, 2)) // should be 17
console.log(goals (12, 16, 5)) // should be 33