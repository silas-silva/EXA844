from flask import Flask, render_template, request, redirect, make_response, session
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder='paginas')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'

@app.route('/')

def counter():
    counter_value = request.args.get('counter',default=0, type=int) + 1
    if 'counterCookies' in request.cookies:
        count = int(request.cookies.get('counterCookies'))
    else:
        count = 1
    sessionTime = 0
    showLogin = ''
    username = ''
    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
        sessionTime = remaining_time
        showLogin = 'none'
    else:
        showLogin = 'block'
    resp = make_response(render_template('counter.html', counterCookies=count, counterHidden=counter_value, session=sessionTime, show=showLogin, username=username))
    resp.set_cookie('counterCookies', str(count + 1).encode('utf-8'), max_age=60*60)
    return resp


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)
    return redirect('/')


if __name__ == '__main__':
        app.run(debug=True)