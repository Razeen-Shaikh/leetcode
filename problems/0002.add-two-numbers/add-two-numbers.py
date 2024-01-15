# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1list = []
        l2list = []
        while l1 or l2:
            if l1:
                l1list.append(str(l1.val))
                l1 = l1.next
            if l2:
                l2list.append(str(l2.val))
                l2 = l2.next
        l1list.reverse()
        l2list.reverse()
        sum = list(str(int("".join(l1list)) + int("".join(l2list))))
        sum.reverse()
        node = temp = ListNode(int(sum[0]))
        for i in range(1, len(sum)):
            temp.next = ListNode(int(sum[i]))
            temp = temp.next
        return node
