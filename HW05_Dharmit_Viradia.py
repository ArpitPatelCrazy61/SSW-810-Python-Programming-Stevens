"""Implement Functions to reverse, find index of substring, find second target and read and organize lines in a file """

from typing import Iterator


def reverse(s: str) -> str:
    """Reverses the string"""
    reverse: str = ''

    for c in s:
        reverse = c + reverse
    return reverse


def substring(target: str, s: str) -> int:
    """Finds the offset of substring in a string"""
    index: int = 0

    if target in s:
        c = target[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(target)] == target:
                    return index
            index += 1
    return -1


def find_second(target: str, string: str) -> int:
    """Finds the second target  """

    return string.find(target, string.find(target)+1)


def get_lines(path: str) -> Iterator[str]:
    """Read the lines and organizing the file"""
    try:
        fp: IO = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Cant open {path}")
    else:
        with fp:
            for line in fp:
                line = line.strip('\n')
                while line.endswith('\\'):
                    line = line[:-1] + fp.readline().strip('\n')

                # if "#" in line:
                #     if line.startswith('#'):
                #         del line
                #     else:
                #         line = line.split('#', 1)[0].strip('\n')
                #         yield line
                # else:
                #     yield line

                if not line.startswith('#'):
                    yield line.split('#')[0]
