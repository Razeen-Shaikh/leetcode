# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(first_list, second_list):
            p1 = first_list
            p2 = second_list
            temp = ListNode(-1)
            p3 = temp

            while(p1 is not None and p2 is not None):
                if(p1.val < p2.val):
                    p3.next = p1
                    p1 = p1.next
                else:
                    p3.next = p2
                    p2 = p2.next
                p3 = p3.next
            while(p1 is not None):
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            while(p2 is not None):
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
            return temp.next
        return merge(list1, list2)
