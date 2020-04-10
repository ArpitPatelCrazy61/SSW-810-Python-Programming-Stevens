"""Functions to check anagrams ,cover alphabets and Web Analyzer"""


from collections import defaultdict, Counter
from typing import List, Tuple, Dict


def anagrams_lst(str1: str, str2: str) -> bool:
    """Checking anagrams using list"""
    if sorted(list(str1.lower())) == sorted(list(str2.lower())):
        return True
    else:
        return False


def anagrams_dd(str1: str, str2: str) -> bool:
    """Checking anagrams using defaultdictionary"""
    dd: Dict[str, str] = defaultdict(int)
    for i in str1:
        dd[i] += 1
    for i in str2:
        dd[i] -= 1
    a: bool = any(dd.values())
    if a is False:
        return True
    return False


def anagrams_cntr(str1: str, str2: str) -> bool:
    """Checking anagrams using counter"""
    return Counter(str1) == Counter(str2)


def covers_alphabet(sentence: str) -> bool:
    """Check if sentence includes one instance of character"""
    return set(sentence.lower()) >= set('abcdefghijklmnopqrstuvwxyz')


def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """List all the weblogs in the list"""
    dd: Dict[str, str] = defaultdict(set)
    for i in weblogs:
        dd[i[0]].add(i[1])

    a: list = list()
    for x, n in dd.items():
        a.append([x, list(n)])
    return sorted(a)
