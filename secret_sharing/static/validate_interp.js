document.getElementById("interp").addEventListener("submit", validate);

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

function checkIsInteger(points, err) {
  var i;
  var xs = [];
  var split = points.split(' ');
  for (i=0; i<split.length; i++) {
    var coord = split[i];
    var elems = coord.split(',');
    var x = parseInt(elems[0], 0);
    var y = parseInt(elems[1], 0);
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
  var err_msg = document.getElementById("input_error");
  var valid = true;

  if (points == "") {
    err_msg.innerHTML = "All fields must be filled in.";
    valid = false;
  }

  // Check that the coordinates are all valid integer pairs
  if (valid) {
    valid = checkIsInteger(points, err_msg);
  }

  if (!valid) {
    ev.preventDefault();
  } else {
    err_msg.innerHTML = "";
  }
}
