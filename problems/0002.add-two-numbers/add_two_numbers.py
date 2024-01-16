"""
This module contains the definition for a singly-linked list and the ListNode class.
"""

from typing import Optional


class ListNode:
    """
    Represents a node in a singly-linked list.

    Attributes:
        val: The value stored in the node.
        next: The reference to the next node in the list.
    """
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:
    """
    This class provides a solution for adding two numbers represented as linked lists.
    """
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented as linked lists.

        Parameters:
        - l1: The first linked list.
        - l2: The second linked list.

        Returns:
        - The sum of the two linked lists.
        """
        l1_list = []
        l2_list = []
        while l1 or l2:
            if l1:
                l1_list.append(str(l1.val))
                l1 = l1.next
            if l2:
                l2_list.append(str(l2.val))
                l2 = l2.next
        l1_list.reverse()
        l2_list.reverse()

        num1 = int("".join(l1_list))
        num2 = int("".join(l2_list))

        result = list(str(num1 + num2))
        result.reverse()

        node = temp = ListNode(int(result[0]))

        for i in range(1, len(result)):
            temp.next_node = ListNode(int(result[i]))
            temp = temp.next_node

        return node
