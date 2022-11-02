# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    i, j, k = 0, 1, 0
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            i += 1
            k += 1
            if i != j:
                nums[i] = nums[j]
            else:
                j += 1
    return i+1, nums
