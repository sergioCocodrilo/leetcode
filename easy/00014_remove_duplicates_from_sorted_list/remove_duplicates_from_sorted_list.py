# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)

def linked_list_from_list(a_list: List[int]) -> ListNode:
    head = None
    for item in a_list:
        node = ListNode(item)
        if head is None:
            head = node
        else:
            insert_node(head, node)
    return head

def insert_node(head: ListNode, node: ListNode) -> None:
    current = head
    while True:
        if current.next is None:
            current.next = node
            break
        else:
            current = current.next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    current = head.next
    focused = head
    while True:
        if current is None or focused is None:
            break
        if current.val == focused.val:
            focused.next = current.next
            current = current.next
        else:
            current = current.next
            focused = focused.next
    return head

if __name__ == '__main__':
    l = [0, 1, 1, 2]
    l = []
    head = linked_list_from_list(l)
    head2 = deleteDuplicates(head)
