"""Test Cases for reverse, find substring, find the second target and read the file and organize it"""

import unittest
from HW05_Dharmit_Viradia import reverse, substring, find_second, get_lines


class ReverseTest(unittest.TestCase):
    def test_reverse(self) -> None:
        """Test to reverse the string"""
        self.assertEqual(reverse('abc'), 'cba')
        self.assertEqual(reverse('123'), '321')
        self.assertEqual(reverse('1'), '1')
        self.assertEqual(reverse(' '), ' ')


class SubStringTest(unittest.TestCase):
    def test_substring(self) -> None:
        """Test to find the offset of substring"""
        self.assertEqual(substring("he", "hello"), 0)
        self.assertEqual(substring("ell", "hello"), 1)
        self.assertEqual(substring("xxx", "hello"), -1)
        self.assertEqual(substring("lo", "hello"), 3)


class FindSecondTest(unittest.TestCase):
    def test_find_second(self) -> None:
        """Test to find the second occurence in a string"""
        self.assertEqual(find_second("abba", "abbabba"), 3)
        self.assertEqual(find_second("iss", "Mississippi"), 4)
        self.assertEqual(find_second("xxx", "adb"), -1)


class GetLinesTest(unittest.TestCase):
    def test_get_lines(self) -> None:
        """Test to read file and organize it"""
        file_name: str = 'HW05_Test.txt'
        expect: List[str] = ['<line0>', '<line1>', '<line2>',
                             '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        result: List[str] = list(get_lines(file_name))
        self.assertEqual(result, expect)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
