# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s: str) -> int:
    j = len(s) - 1
    rv = 0
    while s[j] == ' ' and j > 0:
        j -= 1
    while s[j] != ' ' and j >= 0:
        j -= 1
        rv += 1
    return rv
