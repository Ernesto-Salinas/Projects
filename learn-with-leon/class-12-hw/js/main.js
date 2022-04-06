document.getElementById('akali').onclick = akaliFunc
document.getElementById('ahri').onclick = ahriFunc
document.getElementById('irelia').onclick = ireliaFunc


function akaliFunc() {
  document.querySelector('body').style.background = "url(./assets/akali.gif)"
  document.querySelector('body').style.minWidth = '100%'
  document.querySelector('body').style.minheight = '100%'
  document.querySelector('body').style.color = 'white'
}

function ahriFunc() {
  document.querySelector('body').style.background = "url(./assets/ahri.gif)"
  document.querySelector('body').style.minWidth = '100%'
  document.querySelector('body').style.minheight = '100%'
  document.querySelector('body').style.color = 'white'
}

function ireliaFunc() {
  document.querySelector('body').style.background = "url(./assets/irelia.gif)"
  document.querySelector('body').style.minWidth = '100%'
  document.querySelector('body').style.minheight = '100%'
  document.querySelector('body').style.color = 'white'
}
