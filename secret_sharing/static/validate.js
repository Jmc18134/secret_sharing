function validateEncoding() {
  var x = parseInt(document.getElementById("shares").value);
  var y = parseInt(document.getElementById("keys_required").value);
  
  
  if (x < y) {
    alert("N must be greater or equal to K.");
    return false;
  }
}
