document.getElementById("interp").addEventListener("submit", validate);
/*
document.getElementById("show-button").addEventListener("click", thingy);
document.getElementById("eval-button").addEventListener("click", thingy);

function setWhoClicked(ev) {
	this.form.submitted=this.value;
}

function display_poly(ev) {
	console.log(ev.target);
}
*/
function checkAscending(xs, err) {
  var i;
  for (i=1; i<xs.length; i++) {
    if (xs[i] < xs[i-1]) {
      err.innerHTML = "All x values must be increasing.";
      return false
    }
  }
  return true;
}

function checkModx(modulus, x, err) {
  if (valid) {
    var x = parseFloat(x, 10);
    var y = parseInt(modulus, 10);
    if (isNaN(x) || isNaN(y)) {
      err.innerHTML = "X must be a float, the modulus must be a positive integer.";
      return false;
    }
    
    if (y < 1) {
      err.innerHTML = "Modulus must be greater than 0.";
      return false;
    }

    return true;
  }
}

function checkIsInteger(points, err) {
  var i;
  var xs = [];
  var split = points.split(' ');
  for (i=0; i<split.length; i++) {
    var coord = split[i];
    var elems = coord.split(',');
    var x = parseInt(elems[0], 10);
    var y = parseInt(elems[1], 10);
    if (isNaN(x) || isNaN(y)) {
      err.innerHTML = "Invalid coordinates.";
      return false;
    }
    xs.push(x);
  }

  return checkAscending(xs, err);
}

function validate(ev) {
  var points = document.getElementById("points").value;
  var xval = document.getElementById("x-val").value;
  var modulus = document.getElementById("modulus").value;
  var err_msg = document.getElementById("input_error");
  var valid = true;

  if (points == "" || xval == "") {
    err_msg.innerHTML = "All fields must be filled in.";
    valid = false;
  }

  // Check that the coordinates are all valid integer pairs
  if (valid) {
    valid = checkIsInteger(points, err_msg);
  }
 
  // Check that the modulus and x-val are OK
  if (valid && modulus != "") {
    valid = checkModx(modulus, x);
  }

  if (!valid) {
    ev.preventDefault();
  } else {
    err_msg.innerHTML = "";
  }
}
