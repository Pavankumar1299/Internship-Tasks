//  Function for Alert on button click
function showAlert() {
  alert("Button clicked! JavaScript is working.");
}

//  Function for Change text on click
function changeText() {
  document.getElementById("text").innerText =
    "I told you, Text will change!";
}

//  Function for Form validation
function validateForm() {
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;

  if (name === "" || email === "") {
    alert("Please fill all fields");
    return false;
  }

  alert("Form submitted successfully!");
  return true;
}

//  Function for Simple calculator
function calculate() {
  let num1 = Number(document.getElementById("num1").value);
  let num2 = Number(document.getElementById("num2").value);
  let operator = document.getElementById("operator").value;
  let result;

  if (operator === "+") result = num1 + num2;
  else if (operator === "-") result = num1 - num2;
  else if (operator === "*") result = num1 * num2;
  else if (operator === "/") {
    if (num2 === 0) {
      alert("Cannot divide by zero");
      return;
    }
    result = num1 / num2;
  }

  document.getElementById("result").innerText =
    "Result: " + result;
}