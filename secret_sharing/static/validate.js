document.getElementById("encode").addEventListener("submit", validate);

function validate(ev) {
  var shares = parseFloat(document.getElementById("shares").value);
  var keys = parseFloat(document.getElementById("keys_required").value);
  var valid = true;
  var err_msg = document.getElementById("input_error");

  if (shares != NaN && keys != NaN) {
    if (shares < keys) {
      valid = false;
      err_msg.innerHTML = "N must be less than K.";
    }
  } else {
    valid = false;
    err_msg.innerHTML = "N and K must be numbers.";
  }

  if (!valid) {
    ev.preventDefault();
  } else {
    err_msg = "";
  }
}
