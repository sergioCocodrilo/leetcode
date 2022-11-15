# https://leetcode.com/problems/search-insert-position/

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return 0
    # if target < nums[0]:
    #     return 0
    i, j = 0, len(nums) - 1
    while i < j:
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    if target > nums[i]:
        return i + 1
    else:
        return i


if __name__ == '__main__':
    inputs = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([1,3,5,6], 0, 0),
    ]
    for nums, target, expected in inputs:
        print(searchInsert(nums, target), f'{expected = }')
