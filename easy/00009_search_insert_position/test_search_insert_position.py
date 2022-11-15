import pytest
from typing import List
from search_insert_position import searchInsert

@pytest.mark.parametrize('nums, target, expected', [
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 2, 1),
    ([1,3,5,6], 7, 4),
    ([1,3,5,6], 0, 0),
])
def test_searchInsert(nums: List[int], target: int, expected: int) -> None:
    assert searchInsert(nums, target) == expected
