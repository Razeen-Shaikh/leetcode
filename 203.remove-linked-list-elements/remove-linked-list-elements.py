# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        if temp is None:
            return
        while (temp != None) and (temp.val == val):
            head = head.next
            temp = temp.next
        if temp is not None:
            while temp.next != None:
                if temp.next.val == val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        return head
