# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        while head:
            if not head:
                return None
            values.append(head.val)
            head = head.next
        temp = values[k-1]
        values[k-1] = values[len(values)-k]
        values[len(values)-k] = temp
        listNode = node = ListNode(values[0])
        for i in range(1, len(values)):
            node.next = ListNode(values[i])
            node = node.next
        return listNode
