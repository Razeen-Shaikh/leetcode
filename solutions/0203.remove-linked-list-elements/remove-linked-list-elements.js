/**
 * 203. Remove Linked List Elements
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function (head, val) {
	if (head !== null) {
		var n = head;
		while (n !== null && n.val == val) {
			head = head.next;
			n = n.next;
		}
		if (n !== null) {
			while (n.next !== null) {
				if (n.next.val == val) {
					n.next = n.next.next;
				} else n = n.next;
			}
		}
	}
	return head;
};
