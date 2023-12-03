import unittest

from main import alg_parse
from main import parse_list

raw_input = open('data.txt', 'r').read().split('\n')

class TestAlg(unittest.TestCase):
    def test_basic(self):
        """
        Test takes a basic string and returns first and last integer, even written numbers
        """
        str = "12a35"
        result = alg_parse(str)
        self.assertEqual(result, 15)
    
    def test_basic_with_char(self):
        """
        Test that can take a string of numbers and characters and return first and last integer
        """
        str = "2ddbi6"
        result = alg_parse(str)
        self.assertEqual(result, 26)
    
    def test_basic_with_written_number(self):
        """
        Test that can take a string of numbers and characters and return first and last integer
        """
        str = "dd5b2i9one"
        result = alg_parse(str)
        self.assertEqual(result, 51)
    
    def test_with_(self):
        """
        Test that can take a string of numbers and characters and return first and last integer
        """
        str = "1onetwothre5"
        result = alg_parse(str)
        self.assertEqual(result, 15)
    
    def test_stuck_prob(self):
        """
        Testing input
        """
        str = "fourfourthreehnbhkmscqxdfksg64bvpppznkh"
        result = alg_parse(str)
        self.assertEqual(result, 44)

    def test_raw_input(self):
        """
        Testing problem input
        """
        result = parse_list(raw_input)
        self.assertIsInstance(result, int)
        print(result)

if __name__ == '__main__':
    unittest.main()