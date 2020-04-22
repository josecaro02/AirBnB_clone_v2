#!/usr/bin/python3
""" Starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def index():
    states = storage.all(State).values()
    for i in states:
        print(i.id + " -- " + i.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def rm_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
