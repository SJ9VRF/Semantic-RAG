# Tests for storage manager
import unittest
from unittest.mock import patch
from src.storage import StorageManager

class TestStorageManager(unittest.TestCase):
    @patch('builtins.open', unittest.mock.mock_open())
    def test_save_and_load(self):
        storage = StorageManager(config={})
        storage.save({'key': 'value'}, 'test_key')
        data = storage.load('test_key')
        self.assertEqual(data, {'key': 'value'})

if __name__ == '__main__':
    unittest.main()
