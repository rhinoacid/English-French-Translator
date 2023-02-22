import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def testEnglish_to_french(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"),"Hello")

    def testFrench_to_english(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"),"Bonjour")

if __name__ == '__main__':
    unittest.main()