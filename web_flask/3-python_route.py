#!/usr/bin/python3
"""start flask app"""


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_bnb():
    """say hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def bnb_page():
    """say HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def hello_c(text):
    """display text"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def hello_python(text):
    """display text"""
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    """run in cmd"""
    app.run(host='0.0.0.0', port=5000)
