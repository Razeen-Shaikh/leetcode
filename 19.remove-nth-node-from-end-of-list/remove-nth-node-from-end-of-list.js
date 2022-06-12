/**
 * 19. Remove Nth Node From End of List
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
	var list = head,
		temp = head,
		len = 0;
	while (list !== null) {
		len++;
		list = list.next;
	}
	if (len - n === 0) {
		head = temp.next;
		return head;
	}
	for (i = 0; i < len - n - 1 && temp !== null; i++) {
		temp = temp.next;
	}
	if (temp == null || temp.next == null) return head;
	var node = temp.next.next;
	temp.next = node;

	return head;
};
