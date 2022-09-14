#!/usr/bin/python3
"""
Flask application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_session(response):
    """ Teardown method"""
    storage.close()


@app.route('/states_list')
def states_list():
    """ index for the route /states_list route """
    states = storage.all(State)
    return render_template('7-states_list.html',
                           items=states.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
