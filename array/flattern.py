
"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable
def flattern(arr, output=None):
    if output is None:
        output = []
    for ele in arr:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            flattern(ele, output)
        else:
            out.append(ele)
    return output
def flattern_iter(iterable):
    for ele in iterable:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            yield from flattern_iter(ele)
        else:
            yield ele