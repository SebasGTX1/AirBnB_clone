#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from console import HBNBCommand
from models.user import User
from models.base_model import BaseModel
import console
import unittest


class TestConsole(unittest.TestCase):
    """ Testing the HBNBCommand class of the Console """

    def test_documentation(self):
        """ Testing module docstrings documentation"""

        self.assertTrue(console.__doc__)
        self.assertTrue(console.HBNBCommand.__doc__)

    def test_methods_doc(self):
        """ Testing all docstrings documentation of each console method"""

        for all_methods in dir(HBNBCommand):
            self.assertTrue(all_methods.__doc__)


if __name__ == '__main__':
    unittest.main()
