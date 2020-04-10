"""Test Cases for copy list, intersect list, different list, remove vowels, password checking and insertion sort"""

import unittest
from HW06_Dharmit_Viradia import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, DonutQueue


class ListTest(unittest.TestCase):

    def test_list_copy(self) -> None:
        """Test for list copy"""
        self.assertEqual(list_copy([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(list_copy([]), [])
        self.assertEqual(list_copy([0, "abc", "def"]), [0, "abc", "def"])

    def test_list_difference(self) -> None:
        """Test for difference of a list using list comprehension"""
        self.assertEqual(list_difference(
            [1, 2, 3, 4], [1, 2, 5, 6, 7]), [3, 4])
        self.assertEqual(list_difference([1, 2, 3], [1, 2, 4]), [3])
        self.assertEqual(list_difference([1, 2, 3], [4, 5, 6]), [1, 2, 3])

    def test_list_intersect(self) -> None:
        """Test for intersection of two list"""
        self.assertEqual(list_intersect(
            [1, 2, 3, 4], [1, 3, 4, 6, ]), [1, 3, 4])
        self.assertEqual(list_intersect([1, 2, 3], [1, 2, 4]), [1, 2])
        self.assertEqual(list_intersect([1, 2, 3], [4, 5, 6]), [])

    def test_remove_vowels(self) -> None:
        """Test for removal of vowels from string"""
        self.assertEqual(remove_vowels('Aeiou'), '')
        self.assertEqual(remove_vowels('hellohi'), 'hellohi')
        self.assertEqual(remove_vowels(
            "Amy is my favorite daughter"), "my favorite daughter")
        self.assertEqual(remove_vowels(
            'Jan is my best friend'), "Jan my best friend")
        self.assertEqual(remove_vowels(''), '')

    def test_check_pwd(self) -> None:
        """Test for checking the password authenticity"""
        self.assertEqual(check_pwd('1SteVens'), True)
        self.assertEqual(check_pwd('Ste@1vEns1'), False)
        self.assertEqual(check_pwd('abcdef'), False)
        self.assertEqual(check_pwd('1ABcdef'), True)
        self.assertEqual(check_pwd(''), False)


class DonutQueueTest(unittest.TestCase):
    def test_queue(self) -> None:
        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
