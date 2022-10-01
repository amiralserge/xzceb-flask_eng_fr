import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(english_to_french(""), "", "Failed")

    def test_non_null_import(self):
        self.assertNotEqual(english_to_french("Hello"), "", "Bonjour didnt get translate")

class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(french_to_english(""), "", "Empty string should not be translated")
        
    def test_not_null_input(self):
        self.assertNotEqual(french_to_english("Bonjour"), "", "Translation should not be empty")

unittest.main()
