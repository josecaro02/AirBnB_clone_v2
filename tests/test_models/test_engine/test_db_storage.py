#!/usr/bin/python3
"""test for state"""
import unittest
from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage, DBStorage
import MySQLdb
import pep8

DUser = environ.get('HBNB_MYSQL_USER')
pwd = environ.get('HBNB_MYSQL_PWD')
hots = environ.get('HBNB_MYSQL_HOST')
dbase = environ.get('HBNB_MYSQL_DB')


class TestDB(unittest.TestCase):
    """ Test State Class in DB storage """

    def test_pep8_DB(self):
        """Test pep8 """
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(check.total_errors, 0, "View Pep8")
