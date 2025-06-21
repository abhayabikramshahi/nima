// script.js - Login validation for FSOCIETY

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const errorDiv = document.getElementById('error-message');

    if (username === 'admin' && password === 'nima') {
        errorDiv.textContent = '';
        localStorage.setItem('fsociety_logged_in', 'true');
        window.location.href = '/Account/dashboard.html'; // Redirect to dashboard
    } else {
        errorDiv.textContent = 'Invalid username or password. Please try again.';
    }
});
