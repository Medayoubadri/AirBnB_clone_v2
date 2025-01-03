#!/usr/bin/python3
"""Unit test for review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test cases for review class"""

    def __init__(self, *args, **kwargs):
        """Test initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place_id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test text """
        new = self.value()
        self.assertEqual(type(new.text), str)
