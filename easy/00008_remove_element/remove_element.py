# https://leetcode.com/problems/remove-element/

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i, j = 0, len(nums) - 1
    if i == j:
        if nums[i] == val:
            return 0, nums
        else:
            return 1, nums
    while i < j:
        while nums[i] != val and i < j:
            i += 1
        while nums[j] == val and j > i:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        print(f'{nums = }, {i = }, {j = }')
    if i == j and nums[i] != val:
        i += 1
    return i, nums

