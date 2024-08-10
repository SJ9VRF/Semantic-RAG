# Tests for data_processing
import unittest
from src.data_processing import DataProcessor, Element

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()

    def test_process_item(self):
        # Test processing of a simple text element
        raw_element = Element(type='text', content='  Example  ')
        processed = self.processor.process_item(raw_element)
        self.assertEqual(processed.content, 'Example')  # Assuming trimming spaces

if __name__ == '__main__':
    unittest.main()
