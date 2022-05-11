// Event Listeners to watch for clicks for each champion
document.getElementById('akali').onclick = akaliFunc
document.getElementById('ahri').onclick = ahriFunc
document.getElementById('irelia').onclick = ireliaFunc
document.getElementById('jhin').onclick = jhinFunc
document.getElementById('kayn').onclick = kaynFunc
document.getElementById('kennen').onclick = kennenFunc
document.getElementById('leeSin').onclick = leeSinFunc
document.getElementById('shen').onclick = shenFunc
document.getElementById('zed').onclick = zedFunc

// variables for Media Query Listeners
var akaliVpCond = window.matchMedia("(max-aspect-ratio: 3/2)")


// Media Query listeners to check the state of the viewport and check for changes in viewport size
akaliVpCond.addListener(akaliMedia)

// Media Query Function to change background width and height depending on aspect ratio of viewport
function akaliMedia(){
  if (bgvar==='akali'){
    if (akaliVpCond.matches){
      document.querySelector('body').style.backgroundSize = "auto 100%"
      document.querySelector('body').style.backgroundPosition = "center"
    } else{
      document.querySelector('body').style.backgroundSize = "100% auto"
      document.querySelector('body').style.backgroundPosition = "center top"
    }
  }
}



function akaliFunc() {
  bgvar='akali'
  document.querySelector('body').style.background = "url(./assets/akali.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  akaliMedia()
  document.querySelector('body').style.color = 'white'
}

function ahriFunc() {
  bgvar='ahri'
  document.querySelector('body').style.background = "url(./assets/ahri.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}

function ireliaFunc() {
  bgvar='irelia'
  document.querySelector('body').style.background = "url(./assets/irelia.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}

function jhinFunc() {
  bgvar='jhin'
  document.querySelector('body').style.background = "url(./assets/jhin.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}

function kaynFunc() {
  bgvar='kayn'
  document.querySelector('body').style.background = "url(./assets/kayn.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}

function kennenFunc() {
  bgvar='kennen'
  document.querySelector('body').style.background = "url(./assets/kennen.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}

function leeSinFunc() {
  bgvar='leeSin'
  document.querySelector('body').style.background = "url(./assets/leesin.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}

function shenFunc() {
  letbgvar='shen'
  document.querySelector('body').style.background = "url(./assets/shen.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}

function zedFunc() {
  bgvar='zed'
  document.querySelector('body').style.background = "url(./assets/zed.gif)"
  document.querySelector('body').style.backgroundRepeat = "no-repeat"
  document.querySelector('body').style.backgroundSize = '100% 100%'
  document.querySelector('body').style.color = 'white'
}