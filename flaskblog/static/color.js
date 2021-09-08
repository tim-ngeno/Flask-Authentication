var colors = ["gray", "red", "green", "blue", "orange", "yellow", "purple", "pink"];
var rotateOffset = 0;

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
  setColours();
});

document.getElementById('clockwise').addEventListener("click", () => {
  rotateOffset++
  setColours();
});

var e = document.getElementById("color");
// var strUser = e.options[e.selectedIndex].text;

//function saveColor(t) {
//  var url = "/register";
//  var data = {color: $(e.options[e.selectedIndex].val())};
//  $.post(url, data);
//}


