import unittest
import dic_program

class TestDict(unittest.TestCase):
    def test_dictionary(self):
        d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
        result = dic_program.ClassDict().return_dict()        
        self.assertEqual(result, d)