document.getElementById("encode").addEventListener("submit", validate);

function validate(ev) {
  var shares = document.getElementById("shares").value;
  var keys = document.getElementById("keys_required").value;
  var secret = document.getElementById("secret").value;
  var valid = true;
  var err_msg = document.getElementById("input_error");

  if (shares == "" || keys  == "" || secret == "") {
      err_msg.innerHTML = "All fields must be filled in.";
      valid = false;
  }

  shares = parseInt(shares)
  keys = parseInt(keys)
  secret = parseInt(secret)

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
