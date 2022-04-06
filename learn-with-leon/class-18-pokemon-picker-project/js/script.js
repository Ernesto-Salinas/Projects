let counter = 0;
const mainHolder = document.querySelector("#main")
const spanHolder = document.querySelector("#testImage");
const sectionHolder = document.querySelector("#pokemonImage");

sectionHolder.addEventListener('click', revealNextPokemon);

console.log(counter);

function revealNextPokemon() {
  // let pokemonReveal = false;
  let pokemonSilhouetteArray = ["https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/mewtwo-silhouette.png?v=1646963773263",
                               "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/mewtwo.png?v=1646963770621",
                               // "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/milotic-silhouette.png?v=1646962434094",
                               // "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/milotic.png?v=1646962429624",
                               // "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/absol-silhouette.png?v=1646963540980",
                               // "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/absol.png?v=1646960721616",
                               "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/squirtle-silhouette.png?v=1646963373864",
                               "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/squirtle.png?v=1646959974939",
                               "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/hitmonlee-silhouette.png?v=1646963886736",
                               "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/hitmonlee.png?v=1646963858292",
                               "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/IMG_1111.PNG?v=1646965507390",
                               "https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/IMG_4556.PNG?v=1646960129954"];
  // let pokemonRevealArray = ["",
  //                          "",
  //                          "",
  //                          "",
  //                          ""];
  let image;
  
  
  //checks if we're on a silhouette image or pokemon reveal image
  // if (!pokemonReveal) {
    image = pokemonSilhouetteArray[counter];
  // }
  // } else {
  //   image = pokemonRevealArray[counter];
  // }
  //sets image in section 
  spanHolder.style.background = `url(${image}) no-repeat`;
  spanHolder.style.backgroundSize = `contain`
  // spanHolder.style.width="500px";
  // spanHolder.style.height="500px";
  spanHolder.style.width="50%";
  spanHolder.style.height="50%";
  
  

  // should flip between arrays to select correct image
  // pokemonReveal = !pokemonReveal;
  
  if (counter % 2 === 0) {
    playWhosThatPokemonAudio();
  } else {
    playRevealAudio();
  }
  
    //increments counter to move through array
  if (counter === pokemonSilhouetteArray.length - 1) {
    counter = 0;
  } else {
    counter += 1;
  }
}

function playWhosThatPokemonAudio() {
  var audio = new Audio("https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/Audio2.mp3?v=1646968185537");
  audio.play();
}

function playRevealAudio() {
  if (counter === 1) {
      var audio = new Audio("https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/Mewto.mp3?v=1646970194036");
  audio.play();
  } else if (counter === 3) {
      var audio = new Audio("https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/Squirtle.mp3?v=1646970187816");
  audio.play();
  } else if (counter === 5) {
      var audio = new Audio("https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/Hitmonlee.mp3?v=1646970201676");
  audio.play();
  } else if (counter === 7) {
          var audio = new Audio("https://cdn.glitch.global/60c58ca5-d634-49cc-8f40-b102cd83541c/Leon2.mp3?v=1646970952656");
  audio.play();
  }
}