#!/usr/bin/python3
"""Unit test for amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Tests for Amenity class """

    def __init__(self, *args, **kwargs):

        """
        Initializes an instance of test_Amenity

        Args:
            *args (list): Arguments to be passed to the parent class
            **kwargs (dict): Keyword arguments to be passed to the parent class

        Attributes:
            name (str): Name of the class being tested
            value (Amenity): Instance of the class being tested
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):

        """Checks that Amenity has a name attribute which is a string"""
        new = self.value()
        self.assertEqual(type(new.name), str)
