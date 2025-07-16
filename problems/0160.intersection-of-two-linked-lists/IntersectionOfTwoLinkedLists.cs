public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution
{
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        if (headA == null || headB == null)
        {
            return null;
        }

        ListNode pA = headA, pB = headB;

        while (pA != pB)
        {
            pA = (pA != null) ? pA.next : headB;
            pB = (pB != null) ? pB.next : headA;
        }

        return pA;
    }
}