#!/usr/bin/python3
""" Starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def index():
    states = storage.all(State).values()
    sort_states = sorted(list(states), key=lambda k: k.name)
    cities = storage.all(City).values()
    sort_cities = sorted(list(cities), key=lambda k: k.name)
    return render_template('8-cities_by_states.html', states=sort_states,
                           cities=sort_cities)


@app.teardown_appcontext
def rm_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
