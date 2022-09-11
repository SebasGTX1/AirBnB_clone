#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Testing module for user"""

def __init__(self, *args, **kwargs):
        """ Constructor method """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Testing name """
        new = self.value(first_name="Name")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Testing last name """
        new = self.value(last_name="Last name")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Testing mail """
        new = self.value(email="email@holberton.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Testing  password """
        new = self.value(password="helloworld")
        self.assertEqual(type(new.password), str)
