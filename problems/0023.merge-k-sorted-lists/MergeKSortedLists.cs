/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

using System.Collections.Generic;
using System.Linq;

public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class MergeKSortedLists
{
    public ListNode MergeKLists(ListNode[] lists)
    {
        if (lists == null || lists.Length == 0) return null;

        PriorityQueue<ListNode, int> minHeap = new PriorityQueue<ListNode, int>();

        foreach (var list in lists)
        {
            if (list != null) minHeap.Enqueue(list, list.val);
        }

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (minHeap.Count > 0)
        {
            ListNode node = minHeap.Dequeue();
            current.next = node;
            current = current.next;

            if (node.next != null)
            {
                minHeap.Enqueue(node.next, node.next.val);
            }
        }

        return dummy.next;
    }
}