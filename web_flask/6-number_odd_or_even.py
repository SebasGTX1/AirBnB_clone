#!/usr/bin/python3
"""
Flask application
"""
from flask import Flask, render_template


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
    Index entry for route /number/
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    Index entry for route /number_template/
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Index entry for route /number_odd_or_even/<n>"""
    _is = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n, even_odd=_is)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
