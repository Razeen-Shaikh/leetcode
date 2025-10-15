/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function (head) {
  if (!head) return null;

  let curr = head;
  while (curr) {
    const copy = new Node(curr.val, curr.next, null);
    curr.next = copy;
    curr = copy.next;
  }

  curr = head;
  while (curr) {
    if (curr.random) {
      curr.next.random = curr.random.next;
    }
    curr = curr.next.next;
  }

  curr = head;
  const pseudoHead = new Node(0);
  let copyCurr = pseudoHead;

  while (curr) {
    const copy = curr.next;
    copyCurr.next = copy;
    copyCurr = copy;

    curr.next = copy.next;
    curr = curr.next;
  }

  return pseudoHead.next;
};
