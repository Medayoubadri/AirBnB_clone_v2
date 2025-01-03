#!/usr/bin/python3
"""Unittest for base model"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Test cases for BaseModel class """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the test class.

        Sets the name and value attributes of the class instance.
        """
        """"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Sets up test environment.

        Deletes any existing 'file.json' file from previous runs.
        """
        pass

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """Test default value"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Creates an instance of the class using the to_dict method.
        Then it asserts that the two instances are not the same.
        """
        """"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Test kwargs with non-dict """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test __str__ method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ Test to_dict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """test kwargs none """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """test kwargs one """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """test id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test created_at """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """test updated_at """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
