#!/usr/bin/python3
'''Testing file_storage.py'''
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
all_data = storage.all()


class TestFileStorage(unittest.TestCase):
    '''Testing FileStorage'''
    def test_all(self):
        '''Testing all method'''
        storage = FileStorage()
        self.assertIsNotNone(all_data)
        self.assertEqual(dict, type(all_data))
        self.assertIs(all_data, storage._FileStorage__objects)

    def test_new(self):
        '''Testing new mwthod'''
        storage = FileStorage()
        saitama = User()
        saitama.id = 75342
        saitama.first_name = 'Saitama'
        saitama.last_name = 'calvo'
        storage.new(saitama)
        k = saitama.__class__.__name__ + '.' + str(saitama.id)
        self.assertIsNotNone(all_data[k])

    def test_save(self):
        '''Testing save method'''
        storage = FileStorage()
        '''storage.save()
        exist = os.path.exists('file.json')
        self.assertTrue(exist)'''
        with self.assertRaises(TypeError):
            storage.save(123)

    def test_reload(self):
        '''Testing reload method'''
        storage1 = FileStorage()
        for all_id in storage1.keys():
            obj = all_data[all_id]
        print(obj)
        self.assertIsNotNone(obj)
        '''with self.assertRaises(TypeError):
            storage.reload(123)'''

if __name__ == "__main__":
    unittest.main()