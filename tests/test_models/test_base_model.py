#!/usr/bin/python3
"""unit test for BaseModel class"""
import unittest
import sys
sys.path.append('../..')
from models.base_model import BaseModel
from unittest.mock import patch, call


class TestBaseModel(unittest.TestCase):
    """Test class of BaseModel"""

    def setUp(self):
        self.model1 = BaseModel()
        self.model1.name = "My First Model"
        self.model1.my_number = 89
        self.model2 = BaseModel()
        self.model2.name = "Second Model"
        self.model2.number = 60

    def tearDown(self):
        pass

    def testUniqueID(self):
        self.assertNotEqual(self.model1.id, self.model2.id)

    def testSave(self):
        self.model1.save()
        self.assertNotEqual(self.model1.created_at, self.model1.updated_at)
        self.model2.save()
        self.assertNotEqual(self.model2.created_at, self.model2.updated_at)

if __name__ == '__main__':
    unittest.main()
