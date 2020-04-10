"""
Implement Functions to count vowels , last occurence , enumerate 

"""


import random
from typing import Any, List, Optional, Sequence, Iterator, Tuple


def count_vowels(s: str) -> int:
    ''' return the number of vowels in the string s '''
    count: int = 0
    vowels: str = ('aeiou')
    for i in s.lower():
        if i in vowels:
            count = count + 1
    return count

    
def last_occurrence(target: Any, seq: Sequence[Any]) -> Optional[int]:
    ''' return the offset from 0 of the last occurrence of target in seq '''
    index: int = None
    for i in range(len(seq)):
        if seq[i] == target:
            index = i
    return index

  

def my_enumerate(seq: Sequence[Any]) -> Iterator[Tuple[int, Any]]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    offset: int = 0
    for item in seq:
        yield offset, item
        offset += 1