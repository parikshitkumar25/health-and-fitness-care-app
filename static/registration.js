document.addEventListener('DOMContentLoaded', function() {
    const registrationForm = document.getElementById('registration-form');
    const usernameField = document.getElementById('username');
    const emailField = document.getElementById('email');
    const passwordField = document.getElementById('password');
    const usernameError = document.getElementById('username-error');
    const emailError = document.getElementById('email-error');
    const passwordError = document.getElementById('password-error');

    registrationForm.addEventListener('submit', function(event) {
        let valid = true;

        if (usernameField.value.trim() === '') {
            usernameError.textContent = 'Username is required';
            valid = false;
        } else {
            usernameError.textContent = '';
        }

        if (emailField.value.trim() === '') {
            emailError.textContent = 'Email is required';
            valid = false;
        } else {
            emailError.textContent = '';
        }

        if (passwordField.value.trim() === '') {
            passwordError.textContent = 'Password is required';
            valid = false;
        } else {
            passwordError.textContent = '';
        }

        if (!valid) {
            event.preventDefault();
        }
    });
});
