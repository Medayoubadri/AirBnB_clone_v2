#!/usr/bin/python3
"""Unit test for city class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
import os
import unittest

class test_City(test_basemodel):
    """Unit test for city class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_city_state_relationship(self):
        state = State(name="California")
        city = City(name="San Francisco", state_id=state.id)
        self.assertEqual(city.state, state)
