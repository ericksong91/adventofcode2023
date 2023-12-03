import unittest

from main import alg_parse
from main import parse_list

class TestSum(unittest.TestCase):
    def test_basic(self):
        """
        Test that can take a string of numbers and return first and last integer
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
    
    def test_basic_with_char_again(self):
        """
        Test that can take a string of numbers and characters and return first and last integer
        """
        str = "dd5b2i9ssd"
        result = alg_parse(str)
        self.assertEqual(result, 59)
    
    # def test_basic_list_of_str(self):
    #     """
    #     Test a list of strings and gather numbers from them and return sum
    #     """
    #     list = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    #     result = parse_list(list)
    #     self.assertEqual(result, 142)

if __name__ == '__main__':
    unittest.main()