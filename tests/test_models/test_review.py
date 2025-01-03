#!/usr/bin/python3
"""
Contains the TestReviewDocs classes
"""

from datetime import datetime
import inspect
import models
from models import review
from models.base_model import BaseModel
import pep8
import unittest


class Test_Review(unittest.TestCase):
    """Test the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up test env by gathering all functions of Review class"""
        cls.review_f = inspect.getmembers(review.Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/review.py is PEP8 compliant"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py is PEP8 compliant"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Ensure that review.py module has a docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Ensure that the Review class has a docstring"""
        self.assertIsNot(review.Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(review.Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Ensure all methods of Review have docstrings"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_review_class_name(self):
        """Test that the class name is 'Review'"""
        self.assertEqual(
            review.Review.__name__, "Review", "Class name should be 'Review'")

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        rev = review.Review()
        self.assertIsInstance(rev, BaseModel)
        self.assertTrue(hasattr(rev, "id"))
        self.assertTrue(hasattr(rev, "created_at"))
        self.assertTrue(hasattr(rev, "updated_at"))

    def test_place_id_attr(self):
        """Test Review has attr place_id, and it's an empty string"""
        rev = review.Review()
        self.assertTrue(hasattr(rev, "place_id"))
        if models.storage_type == 'db':
            self.assertEqual(rev.place_id, None)
        else:
            self.assertEqual(rev.place_id, "")

    def test_user_id_attr(self):
        """Test Review has attr user_id, and it's an empty string"""
        rev = review.Review()
        self.assertTrue(hasattr(rev, "user_id"))
        if models.storage_type == 'db':
            self.assertEqual(rev.user_id, None)
        else:
            self.assertEqual(rev.user_id, "")

    def test_text_attr(self):
        """Test Review has attr text, and it's an empty string"""
        rev = review.Review()
        self.assertTrue(hasattr(rev, "text"))
        if models.storage_type == 'db':
            self.assertEqual(rev.text, None)
        else:
            self.assertEqual(rev.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        rev = review.Review()
        new_d = rev.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in rev.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        rev = review.Review()
        new_d = rev.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], rev.created_at.strftime(time))
        self.assertEqual(new_d["updated_at"], rev.updated_at.strftime(time))

    def test_str(self):
        """test that the str method has the correct output"""
        rev = review.Review()
        string = "[Review] ({}) {}".format(rev.id, rev.__dict__)
        self.assertEqual(string, str(rev))

    def test_init_place_id(self):
        """Test that Review has attr place_id, and it's an empty string"""
        rev = review.Review(place_id="1234")
        self.assertTrue(hasattr(rev, "place_id"))
        self.assertEqual(rev.place_id, "1234")

    def test_init_user_id(self):
        """Test that Review has attr user_id, and it's an empty string"""
        rev = review.Review(user_id="1234")
        self.assertTrue(hasattr(rev, "user_id"))
        self.assertEqual(rev.user_id, "1234")

    def test_init_text(self):
        """Test that Review has attr text, and it's an empty string"""
        rev = review.Review(text="This is a review.")
        self.assertTrue(hasattr(rev, "text"))
        self.assertEqual(rev.text, "This is a review.")
