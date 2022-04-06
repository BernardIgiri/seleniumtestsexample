window.addEventListener("load", () => {
  const form = document.getElementById("login");
  form.addEventListener("submit", e => {
    e.preventDefault();
    const usernameField = document.querySelector("input[name='username']");
    const passwordField = document.querySelector("input[name='password']");
    const submitButton = document.querySelector("button[type='submit']");
    const setDisabled = disabled => {
      usernameField.disabled = disabled;
      passwordField.disabled = disabled;
      submitButton.disabled = disabled;
      form.disabled = disabled;
    }
    setDisabled(true);
    setTimeout(() => {
      setDisabled(false);
      if (usernameField.value === "authorized" && passwordField.value === "password123") {
        document.body.className = "welcome";
      }
    }, 2000);
  });
  document.querySelector("button.logout").addEventListener("click", () => {
    document.body.className = "prompt";
  });
});
