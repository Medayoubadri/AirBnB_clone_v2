#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

from io import StringIO
import os
from unittest.mock import patch
import console
import inspect
import pep8
import unittest
from models.engine.file_storage import FileStorage

HBNBCommand = console.HBNBCommand
pat = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'


class Test_Console(unittest.TestCase):
    """Class for testing documentation of the console"""

    @classmethod
    def setUpClass(cls):
        """Set up the environment before each test."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Reset the environment after each test."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_HBNBCommand_emptyline_docstring(self):
        """Test for the HBNBCommand do_emptyline method docstring"""
        self.assertIsNot(HBNBCommand.emptyline.__doc__, None,
                         "HBNBCommand do_emptyline needs a docstring")
        self.assertTrue(len(HBNBCommand.emptyline.__doc__) >= 1,
                        "HBNBCommand do_emptyline needs a docstring")

    def test_HBNBCommand_do_quit_docstring(self):
        """Test for the HBNBCommand do_quit method docstring"""
        self.assertIsNot(HBNBCommand.do_quit.__doc__, None,
                         "HBNBCommand do_quit needs a docstring")
        self.assertTrue(len(HBNBCommand.do_quit.__doc__) >= 1,
                        "HBNBCommand do_quit needs a docstring")

    def test_HBNBCommand_do_EOF_docstring(self):
        """Test for the HBNBCommand do_EOF method docstring"""
        self.assertIsNot(HBNBCommand.do_EOF.__doc__, None,
                         "HBNBCommand do_EOF needs a docstring")
        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) >= 1,
                        "HBNBCommand do_EOF needs a docstring")

    def test_HBNBCommand_do_create_docstring(self):
        """Test for the HBNBCommand do_create method docstring"""
        self.assertIsNot(HBNBCommand.do_create.__doc__, None,
                         "HBNBCommand do_create needs a docstring")
        self.assertTrue(len(HBNBCommand.do_create.__doc__) >= 1,
                        "HBNBCommand do_create needs a docstring")

    def test_HBNBCommand_do_show_docstring(self):
        """Test for the HBNBCommand do_show method docstring"""
        self.assertIsNot(HBNBCommand.do_show.__doc__, None,
                         "HBNBCommand do_show needs a docstring")
        self.assertTrue(len(HBNBCommand.do_show.__doc__) >= 1,
                        "HBNBCommand do_show needs a docstring")

    def test_HBNBCommand_do_destroy_docstring(self):
        """Test for the HBNBCommand do_destroy method docstring"""
        self.assertIsNot(HBNBCommand.do_destroy.__doc__, None,
                         "HBNBCommand do_destroy needs a docstring")
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) >= 1,
                        "HBNBCommand do_destroy needs a docstring")

    def test_HBNBCommand_do_all_docstring(self):
        """Test for the HBNBCommand do_all method docstring"""
        self.assertIsNot(HBNBCommand.do_all.__doc__, None,
                         "HBNBCommand do_all needs a docstring")
        self.assertTrue(len(HBNBCommand.do_all.__doc__) >= 1,
                        "HBNBCommand do_all needs a docstring")

    def test_HBNBCommand_do_update_docstring(self):
        """Test for the HBNBCommand do_update method docstring"""
        self.assertIsNot(HBNBCommand.do_update.__doc__, None,
                         "HBNBCommand do_update needs a docstring")
        self.assertTrue(len(HBNBCommand.do_update.__doc__) >= 1,
                        "HBNBCommand do_update needs a docstring")

    def test_HBNBCommand_default_docstring(self):
        """Test for the HBNBCommand default method docstring"""
        self.assertIsNot(HBNBCommand.default.__doc__, None,
                         "HBNBCommand default needs a docstring")
        self.assertTrue(len(HBNBCommand.default.__doc__) >= 1,
                        "HBNBCommand default needs a docstring")

    def test_create_missing_class(self):
        """Test create with no class name."""
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        """Test create with an invalid class name."""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        """Test create with invalid syntax."""
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_no_args(self):
        """Test create with no arguments."""
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_with_parameters(self):
        """Test create command with parameters."""
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = 'create State name="California" population=39538223'
            self.assertFalse(HBNBCommand().onecmd(cmd))
            result = output.getvalue().strip()
            self.assertRegex(result, pat)

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            output_str = output.getvalue()
            self.assertIn("California", output_str)
            self.assertIn("39538223", output_str)

        from models.engine.file_storage import FileStorage
        from models.state import State
        storage = FileStorage()
        all_states = storage.all(State)
        self.assertTrue(
            any("California" in str(obj) for obj in all_states.values()))
        self.assertTrue(
            any("39538223" in str(obj) for obj in all_states.values()))
