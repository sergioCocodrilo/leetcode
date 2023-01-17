# https://leetcode.com/problems/add-two-numbers/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

def insert_node(root: ListNode, new_node: ListNode):
    current = root
    while True:
        if current.next is None:
            current.next = new_node
            return
        else:
            current = current.next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    remainder = 0
    result = None
    while l1 or l2 or remainder:
        if l1 and l2:
            new_val   = (l1.val + l2.val + remainder) % 10
            remainder = 0 if (l1.val + l2.val + remainder) < 10 else 1
        elif l1:
            new_val   = (l1.val + remainder) % 10
            remainder = 0 if (l1.val + remainder) < 10 else 1
        elif l2:
            new_val   = (l2.val + remainder) % 10
            remainder = 0 if (l2.val + remainder) < 10 else 1
        else:
            new_val = remainder
            remainder = 0

        if result is None:
            result = ListNode(new_val)
        else:
            insert_node(result, ListNode(new_val))

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return result

def ll_to_list(current: ListNode) -> List[int]:
    '''turn a linked list into a list'''
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result

def list_to_ll(a_list: List[int]) -> ListNode:
    '''turns a list into a linked list'''
    root = ListNode(a_list[0])
    for item in a_list[1:]:
        insert_node(root, ListNode(item))
    return root

if __name__ == '__main__':
    root_a = ListNode(9)
    root_b = ListNode(9)
    for i in range(3):
        insert_node(root_a, ListNode(9))
    for i in range(3, 0, -1):
        insert_node(root_b, ListNode(9))

    result = addTwoNumbers(root_a, root_b)

    #
    while root_a and root_b:
        print(root_a, root_b)
        root_a = root_a.next
        root_b = root_b.next

