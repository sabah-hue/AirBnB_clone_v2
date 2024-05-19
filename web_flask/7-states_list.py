#!/usr/bin/python3
"""start flask app"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_app(exception=None):
    """ remove session """
    storage.close()


@app.route('/states_list')
def display_states():
    """Display states inside html page"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """run in cmd"""
    app.run(host='0.0.0.0', port=5000)
