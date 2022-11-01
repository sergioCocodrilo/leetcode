# https://leetcode.com/problems/palindrome-number/

def isPalindrome(x: int) -> bool:
    input_str = str(x)
    i = 0
    j = len(input_str) - 1
    while(i <= j):
        if input_str[i] != input_str[j]:
            return False
        i += 1
        j -= 1
    return True
