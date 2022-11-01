# https://leetcode.com/problems/longest-common-prefix/

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    count = 0
    while True:
        current = None
        for word in strs:
            if count == len(word):
                return word[:count]
            if current is None:
                current = word[count]
            else:
                if word[count] != current:
                    return word[:count]
        count += 1
