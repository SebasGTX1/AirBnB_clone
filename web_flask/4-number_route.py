#!/usr/bin/python3
"""
Flask application
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    Index entry for route /
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Index entry for route /hbnb
    """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Index entry for route /c/
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    Index entry for route /python/
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """
    Index entry for route /python/
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
