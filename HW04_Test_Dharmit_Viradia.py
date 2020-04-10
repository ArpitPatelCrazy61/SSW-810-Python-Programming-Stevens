"""
Test Functions for count vowels , last occurence , enumerate
"""


import random
import unittest
from typing import Iterator, List, Tuple
from HW04_Dharmit_Viradia import count_vowels, last_occurrence, my_enumerate
    
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self) -> None:
        """ testing count vowels """
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('helLO world'), 3)
        self.assertEqual(count_vowels('hll world'), 1)  
        self.assertEqual(count_vowels(''), 0)  

    
class FindLastTest(unittest.TestCase):
    def test_last_occurrence(self) -> None:
        """ testing last occurrence """
        list = [1, 20, 13, 4, 5, 90]
        self.assertEqual(last_occurrence('p', 'apple'), 2)
        self.assertEqual(last_occurrence(4, list), 3)
        self.assertEqual(last_occurrence(1, list), 0)
        self.assertEqual(last_occurrence(91, list), None)
        self.assertEqual(last_occurrence('2', '1one2two'), 4)

class EnumerateTest(unittest.TestCase):
    def test_enumerate(self) -> None:
        """ test my enumerate by storing the results in a list """
        A = '123abc'
        self.assertEqual(list(my_enumerate(A)), list(enumerate(A)))
        B = ['1', '2', '3', '4', '5', '6', '7']
        self.assertEqual(list(my_enumerate(B)), list(enumerate(B)))
        C = "a", "b", "c", "d"
        self.assertEqual(list(my_enumerate(C)), list(enumerate(C)))
        
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)