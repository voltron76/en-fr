import unittest
from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):

    def english_to_french(self):
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

        result = english_to_french('Good morning')
        self.assertEqual(result, 'Bonjour')

        result = english_to_french(None)
        self.assertIsNone(result)

    def french_to_english(self):
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

        result = french_to_english('Bonne nuit')
        self.assertEqual(result, 'Good night')

        result = french_to_english(None)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()