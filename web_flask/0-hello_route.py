#!/usr/bin/python3
"""start flask app"""


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_bnb():
    """say hello"""
    return "Hello HBNB!"

if __name__ == '__main__':
    """run in cmd"""
    app.run(host='0.0.0.0', port=5000)
