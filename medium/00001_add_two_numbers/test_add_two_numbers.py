import pytest
from typing import List
from add_two_numbers import list_to_ll, ll_to_list, addTwoNumbers

@pytest.mark.parametrize('l1, l2, expected',
    [
        ([2,4,3], [5,6,4], [7,0,8]),
        ([0], [0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
    ]
)
def test_addTwoNumbers(l1: List[int], l2: List[int], expected:List[int]) -> None:
    ll1 = list_to_ll(l1)
    ll2 = list_to_ll(l2)
    result = ll_to_list(addTwoNumbers(ll1, ll2))
    assert result == expected
