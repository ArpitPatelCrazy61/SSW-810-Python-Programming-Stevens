""" Testing check anagrams ,cover alphabets and Web Analyzer"""

import unittest
from HW07_Dharmit_viradia import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer


class TestContainers(unittest.TestCase):
    """This class will test the function for HW07"""

    def test_anagram_lst(self) -> None:
        """Test for anagrams using list"""
        self.assertEqual(anagrams_lst('below', 'elbow'), True)
        self.assertEqual(anagrams_lst('bat', 'tab'), True)
        self.assertEqual(anagrams_lst('', ''), True)
        self.assertEqual(anagrams_lst('12ab', '1a2b'), True)
        self.assertEqual(anagrams_lst('123', ''), False)
        self.assertEqual(anagrams_lst('cinema', 'iceman'), True)
        self.assertEqual(anagrams_lst('dormitory', 'dirtyroom'), True)
        self.assertNotEqual(anagrams_lst('python', 'pthon'), True)
        self.assertEqual(anagrams_lst(" ", " "), True)

    def test_anagrams_dd(self) -> None:
        """Test for anagrams using DefaultDictionary"""
        self.assertEqual(anagrams_dd('below', 'elbow'), True)
        self.assertEqual(anagrams_dd('bat', 'tab'), True)
        self.assertEqual(anagrams_dd('', ''), True)
        self.assertEqual(anagrams_dd('12ab', '1a2b'), True)
        self.assertEqual(anagrams_dd('123', ''), False)
        self.assertEqual(anagrams_dd('cinema', 'iceman'), True)
        self.assertEqual(anagrams_dd('dormitory', 'dirtyroom'), True)
        self.assertNotEqual(anagrams_dd('python', 'pthon'), True)
        self.assertEqual(anagrams_dd(" ", " "), True)

    def test_anagrams_cntr(self) -> None:
        """Test for anagrams using Counter"""
        self.assertEqual(anagrams_cntr('below', 'elbow'), True)
        self.assertEqual(anagrams_cntr('bat', 'tab'), True)
        self.assertEqual(anagrams_cntr('', ''), True)
        self.assertEqual(anagrams_cntr('12ab', '1a2b'), True)
        self.assertEqual(anagrams_cntr('123', ''), False)
        self.assertEqual(anagrams_cntr('cinema', 'iceman'), True)
        self.assertEqual(anagrams_cntr('dormitory', 'dirtyroom'), True)
        self.assertNotEqual(anagrams_cntr('python', 'pthon'), True)
        self.assertEqual(anagrams_cntr(" ", " "), True)

    def test_covers_alphabet(self) -> None:
        """Test to check if sentence includes all instance of alphabets"""
        self.assertEqual(covers_alphabet('AbCdefghiJklomnopqrStuvwxyz'), True)
        self.assertEqual(covers_alphabet(
            'aabbcdefghijklmnopqrstuvwxyzzabc'), True)
        self.assertEqual(covers_alphabet(
            'The quick brown fox jumps over the lazy dog'), True)
        self.assertEqual(covers_alphabet(
            'We promptly judged antique ivory buckles for the next prize'), True)
        self.assertEqual(covers_alphabet(''), False)
        self.assertEqual(covers_alphabet('123'), False)

    def web_analyzer(self) -> None:
        """Test for listing all the weblogs in the list"""
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        summary1: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']), ('google.com', ['Maha', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)
        self.assertNotEqual(web_analyzer(weblogs), summary1)
        self.assertEqual(web_analyzer(''), [])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
