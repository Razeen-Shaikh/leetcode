from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return None

        p1 = head
        p2 = head

        p1 = p1.next
        p2 = p2.next.next

        while p2 and p2.next:
            if p1 == p2:
                break
            p1 = p1.next
            p2 = p2.next.next

        if p1 != p2:
            return None

        p1 = head

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
