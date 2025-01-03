#!/usr/bin/python3
"""Unit test for state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.city import City
import os
import unittest

class test_state(test_basemodel):
    """Test for state class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_state_city_relationship(self):
        state = State(name="California")
        city = City(name="San Francisco", state_id=state.id)
        self.assertIn(city, state.cities)
