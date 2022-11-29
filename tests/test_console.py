#!/usr/bin/python3
"""This is unittest for the console module"""
import sys
import unittest
from console import HBNBCommand
sys.path.append('../')


class TestConsole(unittest.TestCase):
    """Test class for HBNBCommand class"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        pass

    def test_EOF(self):
        pass
