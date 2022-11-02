import pytest
from typing import List
from remove_duplicates_from_sorted_array import removeDuplicates

@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,2], 2, [1, 2,]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0, 1, 2, 3, 4]),
])
def test_removeDuplicates(nums: List[int], k: int, expected: List[int]) -> None:
    k_result, nums_result = removeDuplicates(nums)
    assert k == k_result
    assert nums_result[:k] == expected[:k]
