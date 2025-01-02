#!/usr/bin/python3
"""
Contains the TestConsoleDocs classes
"""

from io import StringIO
from unittest.mock import patch
import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
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


class TestConsoleFunction(unittest.TestCase):
    """Class for testing the console functionality"""

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_with_parameters(self):
        """Test create command with parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            obj_id = f.getvalue().strip()
        self.assertTrue(len(obj_id) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"all State")
            output = f.getvalue()
        self.assertIn("California", output)
        self.assertIn(obj_id, output)


if __name__ == "__main__":
    unittest.main()
