# Tests for pdf_parser
import unittest
from unittest.mock import patch
from src.pdf_parser import PDFParser

class TestPDFParser(unittest.TestCase):
    @patch('src.pdf_parser.partition_pdf')
    def test_parse(self, mock_partition):
        # Setup
        mock_partition.return_value = [{'type': 'text', 'content': 'Example text'}]
        parser = PDFParser(config={})

        # Execution
        result = parser.parse()

        # Assertion
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['content'], 'Example text')

if __name__ == '__main__':
    unittest.main()
