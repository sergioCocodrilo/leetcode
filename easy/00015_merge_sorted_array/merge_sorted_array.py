# https://leetcode.com/problems/merge-sorted-array/

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    i, j, k = m-1, n-1, m+n-1
    while k > -1:
        if  i >= 0 and (j < 0 or nums1[i] >= nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        elif j >= 0 and (i < 0 or nums1[i] < nums2[j]):
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1
            



if __name__ == '__main__':
    tests = [
        # ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        # ([1], 1, [], 0, [1]),
        # ([0], 0, [1], 1, [1]),
        ([2,0], 1, [1], 1, [1,2]),
    ]
    for nums1, m, nums2, n, _ in tests:
        rv = merge(nums1, m, nums2, n)
        print(f'{nums1 = } {rv = }')
