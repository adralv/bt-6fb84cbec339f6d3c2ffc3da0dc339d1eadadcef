// main.js
document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("dark-toggle");
  const body = document.body;

  // Check local storage
  if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-mode");
  }

  toggle?.addEventListener("click", () => {
    body.classList.toggle("dark-mode");

    if (body.classList.contains("dark-mode")) {
      localStorage.setItem("theme", "dark");
    } else {
      localStorage.setItem("theme", "light");
    }
  });
});
