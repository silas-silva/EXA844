from flask import Flask, render_template, request, redirect, session
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder='paginas')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
        return f'Hello, {username}! Your session will expire in '+ str(remaining_time)+' seconds. <a href="/logout">Logout</a>'
    else:
        return 'Welcome to Flask Session Example! <a href="/login">Login</a>'


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)