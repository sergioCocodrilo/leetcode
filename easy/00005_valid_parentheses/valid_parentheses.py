# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    accepted_chars = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    read = []
    for char in s:
        if char in accepted_chars:
            read.append(accepted_chars[char])
        else:
            try:
                expected = read.pop()
                if expected != char:
                    return False
            except IndexError:
                return False
    if len(read) == 0:
        return True
    return False

