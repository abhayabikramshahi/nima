from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'fsociety_secret_key'
app.permanent_session_lifetime = timedelta(days=7)

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'admin'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('rememberMe')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            session['username'] = username
            session.permanent = True if remember else False
            return redirect(url_for('home'))
        else:
            error = 'Invalid login. Try again.'
    return render_template('index.html', error=error)

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/account')
def account():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug=True)
