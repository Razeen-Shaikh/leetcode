/**
 * 206. Reverse Linked List
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
	var current = head,
		next = null,
		reverse = null;
	while (current) {
		next = current.next;
		current.next = reverse;
		reverse = current;
		current = next;
	}

	return reverse;
};
