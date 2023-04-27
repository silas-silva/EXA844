from flask import Flask, render_template, request

app = Flask(__name__, template_folder='paginas')

@app.route('/')
def counter():
    counter_value = request.args.get('counter',default=0, type=int) + 1
    return render_template('counter_hidden.html', counter=counter_value)

if __name__ == '__main__':
    app.run(debug=True)