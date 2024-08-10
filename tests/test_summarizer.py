# Tests for summarizer
import unittest
from unittest.mock import patch
from src.summarizer import Summarizer

class TestSummarizer(unittest.TestCase):
    @patch('src.summarizer.ChatOpenAI')
    def test_summarize(self, mock_chat):
        mock_chat.return_value.summarize.return_value = 'Summary'
        summarizer = Summarizer(config={})
        result = summarizer.summarize(['data'])
        self.assertEqual(result, ['Summary'])

if __name__ == '__main__':
    unittest.main()
