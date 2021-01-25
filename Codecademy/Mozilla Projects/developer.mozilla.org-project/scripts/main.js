let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/corina-veraza.jpg') {
      myImage.setAttribute('src','images/ionia-lor-41.jpg');
    } else {
      myImage.setAttribute('src','images/corina-veraza.jpg');
    }
}
let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');
function setUserName() {
    let myName = prompt('Please enter your name.');
    if(!myName) {
      setUserName();
    } else {
      localStorage.setItem('name', myName);
      myHeading.textContent = `Corina Veraza 
      welcome to Zaun, ${myName}`;
    }
  }
  if(!localStorage.getItem('name')) {
    setUserName();
  } else {
    let storedName = localStorage.getItem('name');
    myHeading.textContent = 'Corina Veraza welcome to Zaun, ' + storedName;
  }
  myButton.onclick = function() {
    setUserName();
  }