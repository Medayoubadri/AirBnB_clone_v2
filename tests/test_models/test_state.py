#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
import models
from models import state
from models.base_model import BaseModel
import pep8
import unittest


class Test_State(unittest.TestCase):
    """Test the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_f = inspect.getmembers(state.State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Test that models/state.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(state.State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(state.State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func_docstrings(self):
        """Test for the presence of docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        stat = state.State()
        self.assertIsInstance(stat, BaseModel)
        self.assertTrue(hasattr(stat, "id"))
        self.assertTrue(hasattr(stat, "created_at"))
        self.assertTrue(hasattr(stat, "updated_at"))

    def test_name_attr(self):
        """Test that State has attribute name, and it's an empty string"""
        stat = state.State()
        self.assertTrue(hasattr(stat, "name"))
        if models.storage_type == 'db':
            self.assertIsNone(stat.name)
        else:
            self.assertEqual(stat.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        stat = state.State()
        new_d = stat.to_dict()
        self.assertIsInstance(new_d, dict)
        self.assertNotIn("_sa_instance_state", new_d)
        for attr in stat.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_d)
        self.assertIn("__class__", new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        stat = state.State()
        new_d = stat.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertIsInstance(new_d["created_at"], str)
        self.assertIsInstance(new_d["updated_at"], str)
        self.assertEqual(new_d["created_at"], stat.created_at.strftime(time))
        self.assertEqual(new_d["updated_at"], stat.updated_at.strftime(time))

    def test_str(self):
        """test that the str method has the correct output"""
        stat = state.State()
        string = "[State] ({}) {}".format(stat.id, stat.__dict__)
        self.assertEqual(string, str(stat))
