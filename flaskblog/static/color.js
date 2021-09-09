var colors = ["gray", "red", "green", "blue", "orange", "yellow", "purple", "pink"];
var rotateOffset = 0;

const USER_COLOR = "yellow"; // chosen by user during sign up


var currentColorPosition = ["gray", "red", "green", "blue", "orange", "yellow", "purple", "pink"];

const charactersLocation = [
  {
    inner: 4,
    outer: 'd',
  },
  {
    inner: 5,
    outer: 'e'
  },
  {
    inner: 6,
    outer: 'f'
  },
  {
    inner: 7,
    outer: 'g'
  },
  {
    inner: 8,
    outer: 'h'
  },
  {
    inner: 1,
    outer: 'a'
  },
  {
    inner: 2,
    outer: 'b'
  },
  {
    inner: 3,
    outer: 'c'
  },
];

function changeColorPosition(old_index, new_index) {
  if (new_index >= currentColorPosition.length) {
      var k = new_index - currentColorPosition.length + 1;
      while (k--) {
          currentColorPosition.push(undefined);
      }
  }
  currentColorPosition.splice(new_index, 0, currentColorPosition.splice(old_index, 1)[0]);
};

function setColours() {
  for (var i = 0; i < colors.length; i++) {
    var arcIndex = (i + rotateOffset) % colors.length;
    document.querySelector("#" + colors[i]).style.strokeDashoffset = (arcIndex ) * -35.3;
  }
}

// Set initial colours
setColours();


    
// Buttons
document.getElementById('anticlockwise').addEventListener("click", () => {
  rotateOffset += (colors.length - 1);
  changeColorPosition(0, currentColorPosition.length - 1);
  setColours();
});

document.getElementById('clockwise').addEventListener("click", () => {
  rotateOffset++;
  changeColorPosition(currentColorPosition.length - 1, 0);
  setColours();
});

document.querySelector('#innerorbit').addEventListener("click", () => {
  const currentColorIndex = currentColorPosition.findIndex(color => color === USER_COLOR);
  const charactersAtIndex = charactersLocation[currentColorIndex];
  document.querySelector('#password').value = document.querySelector('#password').value + charactersAtIndex.inner;
});

document.querySelector('#outerorbit').addEventListener("click", () => {
  const currentColorIndex = currentColorPosition.findIndex(color => color === USER_COLOR);
  const charactersAtIndex = charactersLocation[currentColorIndex];
  document.querySelector('#password').value = document.querySelector('#password').value + charactersAtIndex.outer;
});

var e = document.getElementById("color");
// var strUser = e.options[e.selectedIndex].text;

//function saveColor(t) {
//  var url = "/register";
//  var data = {color: $(e.options[e.selectedIndex].val())};
//  $.post(url, data);
//}


