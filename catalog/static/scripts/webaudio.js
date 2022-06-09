// define variables

let audioCtx;
let source;
let songLength;

const pre = document.querySelector('pre');
const myScript = document.querySelector('script');
const play = document.querySelector('.play');
const stop = document.querySelector('.stop');

const playbackControl = document.querySelector('.playback-rate-control');
const playbackValue = document.querySelector('.playback-rate-value');
playbackControl.setAttribute('disabled', 'disabled');

const loopstartControl = document.querySelector('.loopstart-control');
const loopstartValue = document.querySelector('.loopstart-value');
loopstartControl.setAttribute('disabled', 'disabled');

const loopendControl = document.querySelector('.loopend-control');
const loopendValue = document.querySelector('.loopend-value');
loopendControl.setAttribute('disabled', 'disabled');

const url = document.querySelector('#player').getElementsByTagName('source')[0].src;

// use XHR to load an audio track, and
// decodeAudioData to decode it and stick it in a buffer.
// Then we put the buffer into the source

function getData() {
  if(window.webkitAudioContext) {
    audioCtx = new window.webkitAudioContext();
  } else {
    audioCtx = new window.AudioContext();
  }

  source = audioCtx.createBufferSource();
  request = new XMLHttpRequest();

  request.open('GET', url, true);

  request.responseType = 'arraybuffer';


  request.onload = function() {
    let audioData = request.response;

    audioCtx.decodeAudioData(audioData, function(buffer) {
        myBuffer = buffer;
        songLength = buffer.duration;
        source.buffer = myBuffer;
        source.playbackRate.value = playbackControl.value;
        source.connect(audioCtx.destination);
        source.loop = true;

        loopstartControl.setAttribute('max', Math.floor(songLength));
        loopendControl.setAttribute('max', Math.floor(songLength));
      },

      function(e){"Error with decoding audio data" + e.error});

  }

  request.send();
}

// wire up buttons to stop and play audio, and range slider control

play.onclick = function() {
  getData();
  source.start(0);
  play.setAttribute('disabled', 'disabled');
  playbackControl.removeAttribute('disabled');
  loopstartControl.removeAttribute('disabled');
  loopendControl.removeAttribute('disabled');
}

stop.onclick = function() {
  source.stop(0);
  play.removeAttribute('disabled');
  playbackControl.setAttribute('disabled', 'disabled');
  loopstartControl.setAttribute('disabled', 'disabled');
  loopendControl.setAttribute('disabled', 'disabled');
}

playbackControl.oninput = function() {
  source.playbackRate.value = playbackControl.value;
  playbackValue.innerHTML = playbackControl.value;
}

loopstartControl.oninput = function() {
  source.loopStart = loopstartControl.value;
  loopstartValue.innerHTML = loopstartControl.value;
}

loopendControl.oninput = function() {
  source.loopEnd = loopendControl.value;
  loopendValue.innerHTML = loopendControl.value;
}
