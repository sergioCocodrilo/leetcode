import pytest
from typing import List
from two_sum import twoSum

@pytest.mark.parametrize('nums, target, expected', [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
])
def test_twoSum(nums: List, target: int, expected: List):
    assert expected == twoSum(nums, target)
