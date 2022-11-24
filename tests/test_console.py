#!/usr/bin/python3
"""This is unittest for the console module"""
import sys
sys.path.append('../')
from console import HBNBCommand
import unittest


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
