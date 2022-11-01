#https://leetcode.com/problems/two-sum/

from typing import List

def bruteForcetwoSum(nums: List[int], target: int) -> List[int]:
    '''
    time complexity O(n2)
    '''
    summ = []
    for x in range(len(nums) - 1):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]

def twoSum(nums: List[int], target: int) -> List[int]:
    '''
    time complexity O(n)
    '''
    complements = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        if nums[i] in complements:
            return [complements[nums[i]], i]
        else:
            complements[complement] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))
