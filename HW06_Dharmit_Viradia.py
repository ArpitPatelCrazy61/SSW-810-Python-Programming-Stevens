""""Implement Function to copy list, intersect list, different list, remove vowels, password checking and insertion sort"""

from typing import List, Any, Optional
import queue


def list_copy(l: List[Any]) -> List[Any]:
    """Copying of a list using list comprehension method"""
    copy: List[Any] = [item for item in l]
    return copy


def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    """Intersection of a list using list comprehension method"""
    intersect: List[Any] = [item for item in l1 if item in l2]
    return intersect


def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    """Difference between two list using list comprehension method"""
    diff: List[Any] = [item for item in l1 if item not in l2]
    return diff


def remove_vowels(string: str) -> str:
    """Remove vowels from string using list comprehension method"""
    rvow: str = ' '.join([item for item in string.split()
                          if item.lower()[0] not in 'aeiou'])
    return rvow


def check_pwd(password: str) -> bool:
    """Check Password for Two Uppercase, One Lowercase and Starts with Digit"""
    return len(password) >= 4 \
        and len([c for c in password if c.isupper()]) >= 2 \
        and len([c for c in password if c.islower()]) >= 1 \
        and password[0].isdigit()


class Queue:
    """provide queue semnatics"""

    def __init__(self) -> None:
        self.queue: List[Any] = list()

    def arrive(self, name: str) -> None:
        """ add name to the queue"""
        self.queue.append(name)

    def next_customer(self) -> Optional[str]:
        """pop the current customer and return the next person in queue and none if no one is present"""
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def waiting(self) -> List[str]:
        """return all the customer waiting in the queue"""
        return self.queue


class DonutQueue:
    """ handle queue for donut it allows vip customer to serve first than normal customer"""

    def __init__(self) -> None:
        self.vipqueue: Queue = Queue()
        self.standardqueue: Queue = Queue()

    def arrive(self, name: str, vip: bool) -> None:
        """ add name to the queue"""
        if vip:
            self.vipqueue.arrive(name)
        else:
            self.standardqueue.arrive(name)

    def next_customer(self) -> Optional[str]:
        """pop and return the next person in queue and none if no one present"""
        customer: Optinal[str] = self.vipqueue.next_customer()
        if customer is None:
            customer = self.standardqueue.next_customer()
        return customer

    def waiting(self) -> Optional[str]:
        """return all the customer waiting in the queue and None if no one is waiting"""
        everyone: List[str] = self.vipqueue.waiting() + self.standardqueue.waiting()
        if len(everyone) > 0:
            return ", ".join(everyone)
        else:
            return None
