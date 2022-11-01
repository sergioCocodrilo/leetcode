import pytest
from typing import List, Optional
from merge_two_sorted_lists import mergeTwoLists, mergeTwoLists2
from merge_two_sorted_lists import ListNode
from merge_two_sorted_lists import make_linked_list_from_list
from merge_two_sorted_lists import linked_list_to_list

@pytest.mark.parametrize('list1, list2, expected', [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0]),
])
def test_mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode], expected: List[int]) -> None:
    ll1 = make_linked_list_from_list(list1)
    ll2 = make_linked_list_from_list(list2)
    root = mergeTwoLists(ll1, ll2)
    assert linked_list_to_list(root) == expected


@pytest.mark.parametrize('list1, list2, expected', [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0]),
])
def test_mergeTwoLists2(list1: Optional[ListNode], list2: Optional[ListNode], expected: List[int]) -> None:
    ll1 = make_linked_list_from_list(list1)
    ll2 = make_linked_list_from_list(list2)
    root = mergeTwoLists2(ll1, ll2)
    assert linked_list_to_list(root) == expected
