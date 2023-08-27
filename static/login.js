const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

usernameInput.addEventListener('input', (event) => {
  if (usernameInput.value.length < 3) {
    usernameInput.setCustomValidity('Username must be at least 3 characters long.');
  } else {
    usernameInput.setCustomValidity('');
  }
});

passwordInput.addEventListener('input', (event) => {
  if (passwordInput.value.length < 8) {
    passwordInput.setCustomValidity('Password must be at least 8 characters long.');
  } else {
    passwordInput.setCustomValidity('');
  }
});

const loginButton = document.getElementById('login-button');
loginButton.addEventListener('click', (event) => {
  event.preventDefault();

  // Check if the username and password are valid.
  if (usernameInput.value.length < 3) {
    usernameInput.setCustomValidity('Username must be at least 3 characters long.');
    return;
  }

  if (passwordInput.value.length < 8) {
    passwordInput.setCustomValidity('Password must be at least 8 characters long.');
    return;
  }

  // Submit the form to the login view.
  document.getElementById('login-form').submit();
});

