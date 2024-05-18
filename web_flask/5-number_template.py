#!/usr/bin/python3
"""start flask app"""


from flask import Flask, render_template

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


@app.route('/number/<int:n>')
def display_number(n):
    """Display number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def display_html_page(n):
    """Display number inside html page"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """run in cmd"""
    app.run(host='0.0.0.0', port=5000)
