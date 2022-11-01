# https://leetcode.com/problems/roman-to-integer/

from itertools import pairwise

def romanToInt2(s: str) -> int:
    '''
    time complixity O(n)
    '''
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    ignore = False
    total = 0
    for a, b in pairwise(s):
        if ignore:
            ignore = False
            continue
        if roman_values[a] < roman_values[b]:
            total += roman_values[b] - roman_values[a]
            ignore = True
        else:
            ignore = False
            total += roman_values[a]
    if not ignore:
        total += roman_values[s[-1]]
    return total


def romanToInt(s: str) -> int:
    '''
    time complixity O(n)
    '''
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    i = 1
    total = 0
    while i < len(s):
        if values[s[i-1]] < values[s[i]]:
            total +=  values[s[i]] - values[s[i-1]]
            i += 2
        else:
            total += values[s[i-1]]
            i += 1
    if i == len(s):
        total += values[s[-1]]
    return total
