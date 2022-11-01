# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__ (self):
        return str(self.val)

def insert_full_list(root: ListNode, list1: ListNode):
    while list1:
        if root is None:
            root = ListNode(list1.val)
        else:
            insert_node(root, ListNode(list1.val))
        list1 = list1.next
    return root

def pick_node(list1: ListNode, list2: ListNode):
    if list1.val <= list2.val:
        node  = ListNode(list1.val)
        list3 = 0
    else:
        node  = ListNode(list2.val)
        list3 = 1
    return node, list3


def mergeTwoLists2(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    root = None
    while list1 and list2:
        node, list3 = pick_node(list1, list2)
        if root is None:
            root = node
        else:
            insert_node(root, node)
        if list3 == 0:
            list1 = list1.next
        else:
            list2 = list2.next
    root = insert_full_list(root, list1)
    root = insert_full_list(root, list2)
    return root

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    root = None
    while list1 and list2:
        if root is None:
            if list1.val <= list2.val:
                root = ListNode(list1.val)
                list1 = list1.next
            else:
                root = ListNode(list2.val)
                list2 = list2.next
        else:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            insert_node(root, node)
    while list1:
        if root is None:
            root = ListNode(list1.val)
        else:
            insert_node(root, ListNode(list1.val))
        list1 = list1.next
    while list2:
        if root is None:
            root = ListNode(list2.val)
        else:
            insert_node(root, ListNode(list2.val))
        list2 = list2.next
    return root

def make_linked_list_from_list(l: list) -> ListNode:
    root = None
    for item in l:
        node = ListNode(item)
        if root is None:
            root = node
        else:
            insert_node(root, node)
    return root

def insert_node(current: ListNode, node:ListNode) -> None:
    while True:
        if current.next is None:
            current.next = node
            return
        else:
            current = current.next

def linked_list_to_list(current: ListNode) -> List[int]:
    rv = []
    while current:
        rv.append(current.val)
        current = current.next
    return rv


if __name__ == '__main__':
    root = make_linked_list_from_list([0, 5, 3, 1])


