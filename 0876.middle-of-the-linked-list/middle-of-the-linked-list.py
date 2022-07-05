# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        temp = head
        while temp is not None:
            l.append(temp.val)
            temp = temp.next
        for i in range(int(len(l)/2)):
            head = head.next
        return head
