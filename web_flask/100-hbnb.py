#!/usr/bin/python3
""" Starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__, static_url_path='')


@app.route('/hbnb', strict_slashes=False)
def index():
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    sort_states = sorted(list(states), key=lambda k: k.name)
    sort_cities = sorted(list(cities), key=lambda k: k.name)
    sort_amenities = sorted(list(amenities), key=lambda k: k.name)
    sort_places = sorted(list(places), key=lambda k: k.name)
    return render_template('100-hbnb.html', states=sort_states,
                           cities=sort_cities, amenities=sort_amenities,
                           places=sort_places, users=users)


@app.teardown_appcontext
def rm_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
