#!/usr/bin/python3
"""test for state"""
import unittest
from os import environ
from models import *
from models.base_model import BaseModel
import MySQLdb
import pep8

DUser = environ.get('HBNB_MYSQL_USER')
pwd = environ.get('HBNB_MYSQL_PWD')
hots = environ.get('HBNB_MYSQL_HOST')
dbase = environ.get('HBNB_MYSQL_DB')


class TestDB(unittest.TestCase):
    """ Test State Class in DB storage """

    def test_create(self):
        db = MySQLdb.connect(host=hots, user=DUser, passwd=pwd, db=dbase)
        cur = db.cursor()
        sql_1 = "SELECT COUNT(*) FROM states"
        cur.execute(sql_1)
        result_1 = cur.fetchall()[0][0]
        state = State(name="Joseland")
        state.save()
        storage.save()
        db.commit()
        sql_2 = "SELECT COUNT(*) FROM states"
        cur.execute(sql_2)
        result_2 = cur.fetchall()[0][0]
        self.assertEqual(result_1 + 1, result_2)

    def test_pep8_DB(self):
        """Test pep8 """
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(check.total_errors, 0, "View Pep8")
