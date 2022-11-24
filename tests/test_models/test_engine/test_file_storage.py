#!/usr/bin/python3
import unittest
import sys
sys.path.append('../../..')
from io import StringIO
from os.path import exists, getsize
from models.base_model import BaseModel
from models import storage
from unittest.mock import patch, call
"""unit test for FileStorage class"""


class TestFileStorage(unittest.TestCase):
    """Test class of FileStorage"""

    def setUp(self):
        self.model1 = BaseModel()
        self.model1.name = "My First Model"
        self.model1.my_number = 89
        self.model2 = BaseModel()
        self.model2.name = "Second Model"
        self.model2.number = 60

    def tearDown(self):
        pass

    def testAll(self):
        store_dict = storage.all()
        self.assertEqual(len(store_dict), len(storage.__objects))
        self.model1.save()
        store_dict = storage.all()
        storage.reload()
        self.assertEqual(len(store_dict), len(storage.__objects))

    def testSave(self):
        self.model2.save()
        self.assertTrue(exists('file.json'))
        self.assertTrue(getsize('file.json') > 0)

    def testNew(self):
        model3 = BaseModel()
        self.assertIn(model3, storage.__objects.values())

    def testReload(self):
        self.model1.save()
        self.model2.save()
        storage.reload()
        self.assertEqual(len(storage.__objects), 4)

if __name__ == '__main__':
    unittest.main()
