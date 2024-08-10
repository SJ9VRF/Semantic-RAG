# Tests for element_classifier
import unittest
from src.element_classifier import ElementClassifier
from src.data_processing import Element

class TestElementClassifier(unittest.TestCase):
    def test_classify(self):
        classifier = ElementClassifier()
        elements = [Element(type='text', content='data'), Element(type='table', content='data')]
        categories = classifier.classify(elements)
        self.assertIn('text', categories)

if __name__ == '__main__':
    unittest.main()
