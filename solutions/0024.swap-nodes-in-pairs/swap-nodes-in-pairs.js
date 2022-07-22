/**
 * 24. Swap Nodes in Pairs
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
var swapPairs = function (head) {
	let res = head;
	while (res && res.next) {
		let temp = res.val;
		res.val = res.next.val;
		res.next.val = temp;
		res = res.next.next;
	}
	return head;
};
