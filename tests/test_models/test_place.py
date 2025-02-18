#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""

from datetime import datetime
import inspect
import models
from models import place
from models.base_model import BaseModel
import pep8
import unittest


class Test_Place(unittest.TestCase):
    """Test the Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_f = inspect.getmembers(place.Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """Test for the place.py module docstring"""
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(place.Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(place.Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func_docstrings(self):
        """Test for the presence of docstrings in Place methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_place_func_docstrings(self):
        """Test for the presence of docstrings in Place methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        plass = place.Place()
        self.assertIsInstance(plass, BaseModel)
        self.assertTrue(hasattr(plass, "id"))
        self.assertTrue(hasattr(plass, "created_at"))
        self.assertTrue(hasattr(plass, "updated_at"))

    def test_city_id_attr(self):
        """Test Place has attr city_id, and it's an empty string"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "city_id"))
        if models.storage_type == 'db':
            self.assertEqual(plass.city_id, None)
        else:
            self.assertEqual(plass.city_id, "")

    def test_user_id_attr(self):
        """Test Place has attr user_id, and it's an empty string"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "user_id"))
        if models.storage_type == 'db':
            self.assertEqual(plass.user_id, None)
        else:
            self.assertEqual(plass.user_id, "")

    def test_name_attr(self):
        """Test Place has attr name, and it's an empty string"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "name"))
        if models.storage_type == 'db':
            self.assertEqual(plass.name, None)
        else:
            self.assertEqual(plass.name, "")

    def test_description_attr(self):
        """Test Place has attr description, and it's an empty string"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "description"))
        if models.storage_type == 'db':
            self.assertEqual(plass.description, None)
        else:
            self.assertEqual(plass.description, "")

    def test_number_rooms_attr(self):
        """Test Place has attr number_rooms, and it's an int == 0"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "number_rooms"))
        if models.storage_type == 'db':
            self.assertEqual(plass.number_rooms, None)
        else:
            self.assertEqual(type(plass.number_rooms), int)
            self.assertEqual(plass.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Place has attr number_bathrooms, and it's an int == 0"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "number_bathrooms"))
        if models.storage_type == 'db':
            self.assertEqual(plass.number_bathrooms, None)
        else:
            self.assertEqual(type(plass.number_bathrooms), int)
            self.assertEqual(plass.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test Place has attr max_guest, and it's an int == 0"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "max_guest"))
        if models.storage_type == 'db':
            self.assertEqual(plass.max_guest, None)
        else:
            self.assertEqual(type(plass.max_guest), int)
            self.assertEqual(plass.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test Place has attr price_by_night, and it's an int == 0"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "price_by_night"))
        if models.storage_type == 'db':
            self.assertEqual(plass.price_by_night, None)
        else:
            self.assertEqual(type(plass.price_by_night), int)
            self.assertEqual(plass.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Place has attr latitude, and it's a float == 0.0"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "latitude"))
        if models.storage_type == 'db':
            self.assertEqual(plass.latitude, None)
        else:
            self.assertEqual(type(plass.latitude), float)
            self.assertEqual(plass.latitude, 0.0)

    def test_longitude_attr(self):
        """Test Place has attr longitude, and it's a float == 0.0"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "longitude"))
        if models.storage_type == 'db':
            self.assertEqual(plass.longitude, None)
        else:
            self.assertEqual(type(plass.longitude), float)
            self.assertEqual(plass.longitude, 0.0)

    @unittest.skipIf(models.storage_type == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """Test Place has attr amenity_ids, and it's an empty list"""
        plass = place.Place()
        self.assertTrue(hasattr(plass, "amenity_ids"))
        self.assertEqual(type(plass.amenity_ids), list)
        self.assertEqual(len(plass.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        plass = place.Place()
        new_d = plass.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in plass.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        plass = place.Place()
        new_d = plass.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], plass.created_at.strftime(time))
        self.assertEqual(new_d["updated_at"], plass.updated_at.strftime(time))

    def test_str(self):
        """test that the str method has the correct output"""
        plass = place.Place()
        string = "[Place] ({}) {}".format(plass.id, plass.__dict__)
        self.assertEqual(string, str(plass))
