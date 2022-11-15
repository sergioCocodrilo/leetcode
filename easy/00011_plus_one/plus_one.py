# https://leetcode.com/problems/plus-one/

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    a = 0
    for digit in range(len(digits) - 1, -1, -1):
        to_add = 1 if a == 0 else a
        a, digits[digit] = divmod(digits[digit] + to_add, 10)
        if a == 0:
            break
    if a != 0:
        return [a] + digits
    return digits

if __name__ == '__main__':
    for digits, expected in [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
    ]:
        plusOne(digits)
