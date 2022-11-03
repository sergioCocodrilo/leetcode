import pytest
from typing import List
from remove_element import removeElement

@pytest.mark.parametrize('nums, val, k, expected', [
    ([3,2,2,3], 3, 2, [2,2,]),
    ([0,1,2,2,3,0,4,2], 2, 5, [0,1,4,0,3,]),
    ([2], 3, 1, [2]),
    ([1], 1, 0, []),
    ([3, 3], 5, 2, [3, 3]),
])
def test_removeElement(nums: List[int], val: int, k: int, expected: List[int]) -> None:
    k_result, result = removeElement(nums, val)
    assert k_result == k
    assert result[:k] == expected[:k]
