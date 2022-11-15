import pytest
from typing import List
from plus_one import plusOne

@pytest.mark.parametrize('digits, expected', [
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([9], [1,0]),
])
def test_PlusOne(digits: List[int], expected: List[int]) -> None:
    assert plusOne(digits) == expected
