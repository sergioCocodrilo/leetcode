import pytest
from typing import List
from merge_sorted_array import merge

@pytest.mark.parametrize('nums1, m, nums2, n, expected', [
    ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([2,0], 1, [1], 1, [1,2]),
])
def test_merge(nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]) -> None:
    assert expected == merge(nums1, m, nums2, n)

