#!/usr/bin/python3
"""
Contains the TestAmenityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenity = amenity.Amenity


class Test_Amenity(unittest.TestCase):
    """Test the Amenity class functionality and attributes."""

    @classmethod
    def setUpClass(cls):
        """Set up for doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test models/amenity.py PEP8 conformance"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors")

    def test_pep8_conformance_test_amenity(self):
        """Test tests/test_models/test_amenity.py PEP8 conformance"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors")

    def test_amenity_module_docstring(self):
        """Test for amenity.py module docstring"""
        self.assertTrue(amenity.__doc__)

    def test_amenity_class_docstring(self):
        """Test for Amenity class docstring"""
        self.assertTrue(Amenity.__doc__)

    def test_amenity_func_docstrings(self):
        """Test for docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertTrue(func[1].__doc__)

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """
        Test if Amenity has attribute 'name', and it's an empty string or None
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if models.storage_type == 'db':
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """
        Test to_dict method creates a dictionary with appropriate attributes.
        """
        am = Amenity()
        new_d = am.to_dict()
        self.assertIsInstance(new_d, dict)
        self.assertNotIn("_sa_instance_state", new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_d)
        self.assertIn("__class__", new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertIsInstance(new_d["created_at"], str)
        self.assertIsInstance(new_d["updated_at"], str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the __str__ method has the correct output."""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_id_attr(self):
        """Test that Amenity has an id attribute that is a string."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertIsInstance(amenity.id, str)
