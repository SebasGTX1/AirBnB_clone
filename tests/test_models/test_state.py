#!/usr/bin/python3
""" Testing suit for state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ Initial Testing method"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Testing Name"""
        new = self.value(name="california")
        self.assertEqual(type(new.name), str)
