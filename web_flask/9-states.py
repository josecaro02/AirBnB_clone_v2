#!/usr/bin/python3
""" Starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def index(id):
    states = storage.all(State).values()
    filter_state = None
    sort_states = sorted(list(states), key=lambda k: k.name)
    if id is None:
        sort_cities = None
    else:
        for state in sort_states:
            if state.id == id:
                filter_state = state
        cities = storage.all(City).values()
        sort_cities = sorted(list(cities), key=lambda k: k.name)
    return render_template('9-states.html', states=sort_states,
                           cities=sort_cities, filter_state=filter_state)


@app.teardown_appcontext
def rm_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
