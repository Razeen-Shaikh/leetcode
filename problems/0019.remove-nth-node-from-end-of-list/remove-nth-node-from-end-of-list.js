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
const removeNthFromEnd = function(head, n) {
    let dummy = new ListNode(0);
    dummy.next = head;
    let length = 0;
    let first = head;
    
    while (first !== null) {
        length++;
        first = first.next;
    }
    
    length -= n;
    first = dummy;
    
    for (let i = 0; i < length; i++) {
        first = first.next;
    }
    
    first.next = first.next.next;
    return dummy.next;

};
