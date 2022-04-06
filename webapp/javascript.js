window.addEventListener("load", () => {
  document.getElementById("login").addEventListener("submit", e => {
    e.preventDefault();
    const username = document.querySelector("input[name='username']").value;
    const password = document.querySelector("input[name='password']").value;
    if (username === "authorized" && password === "password123") {
      setTimeout(() => {
        document.body.className = "welcome";
      }, 2);
    }
  });
});
