#!/usr/bin/python3
""" Starts a flask web application """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    message = 'Number: %d' % n
    return render_template('5-number.html', n=message)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_odd_even(n):
    if n % 2 == 0:
        message = 'Number: %d is even' % n
    else:
        message = 'Number: %d is odd' % n
    return render_template('6-number_odd_or_even.html', n=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
