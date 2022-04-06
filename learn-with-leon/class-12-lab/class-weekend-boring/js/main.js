document.querySelector('#check').addEventListener('click', check)

function check() {

  const day = document.querySelector('#day').value

  //Conditionals go here
  if (day == "Sat" || day=="Saturday" || day=="Sun" || day=="Sunday"){
    alert("WEEKEND!!!!! LET'S GO!!!!")
  } else if (day == "Tues" || day=="Tuesday" || day=="Thurs" || day=="Thursday") {
    alert("CLASS!!!")
  } else {
    alert("Boooooooooriiiinnnnnggg")
  }
}
