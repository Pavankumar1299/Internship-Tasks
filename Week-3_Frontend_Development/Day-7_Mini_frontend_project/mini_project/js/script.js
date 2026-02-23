
document.addEventListener("DOMContentLoaded", () => {

  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");
  const contactForm = document.getElementById("contactForm");

  if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Logged in successfully!");

      // save login status
      localStorage.setItem("loggedIn", "true");

      window.location.href = "home.html";
    });
  }

  if (registerForm) {
    registerForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Registered successfully!");

      // auto-login after register
      localStorage.setItem("loggedIn", "true");

      window.location.href = "home.html";
    });
  }

  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Send successfully!");
      window.location.href = "home.html";
    });
  }

});

document.addEventListener("DOMContentLoaded", () => {

  const loginLink = document.getElementById("loginLink");
  const registerLink = document.getElementById("registerLink");
  const logoutBtn = document.getElementById("logoutBtn");

  const loggedIn = localStorage.getItem("loggedIn");

  if (loggedIn === "true") {
    if (loginLink) loginLink.style.display = "none";
    if (registerLink) registerLink.style.display = "none";
    if (logoutBtn) logoutBtn.style.display = "inline-block";
  } else {
    if (loginLink) loginLink.style.display = "inline-block";
    if (registerLink) registerLink.style.display = "inline-block";
    if (logoutBtn) logoutBtn.style.display = "none";
  }
});

function watchMS() {
  const loggedIn = localStorage.getItem("loggedIn");

  if (loggedIn === "true") {
    alert("It's a demo project, so movie is not available.");
  } else {
    alert("Please log in to watch the movie.");
    window.location.href = "login.html";
  }
}

function logout() {
  localStorage.removeItem("loggedIn");
  alert("Logged out successfully!");
  window.location.href = "login.html";
}