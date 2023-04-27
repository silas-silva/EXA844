from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='paginas')

@app.route('/')
def counter():
    if 'counter' in request.cookies:
        count = int(request.cookies.get('counter'))
    else:
        count = 1
    
    resp = make_response(render_template('counter_cookies.html', counter=count))
    resp.set_cookie('counter', str(count + 1).encode('utf-8'), max_age=60*60)
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)