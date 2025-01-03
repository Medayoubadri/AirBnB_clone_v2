#!/usr/bin/python3
"""Unit test for place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test Place class """

    def __init__(self, *args, **kwargs):
        """ Test initialization """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test city_id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_amenity_ids(self):
        """Test amenity_ids """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
