const addTwoNumbers = require("../problems/0002.add-two-numbers/addTwoNumbers");

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

describe("addTwoNumbers", () => {
  // Test case: Both lists are empty
  test("should return null when both lists are empty", () => {
    let l1 = null;
    let l2 = null;
    let expected = null;
    let result = addTwoNumbers(l1, l2);
    expect(result).toEqual(expected);
  });

  // Test case: One list is empty, the other list has one node
  test("should return the non-empty list when one list is empty", () => {
    let l1 = new ListNode(2);
    let l2 = null;
    let expected = new ListNode(2);
    let result = addTwoNumbers(l1, l2);
    expect(result).toEqual(expected);
  });

  // Test case: One list has one node, the other list is empty
  test("should return the non-empty list when one list is empty", () => {
    let l1 = null;
    let l2 = new ListNode(2);
    let expected = new ListNode(2);
    let result = addTwoNumbers(l1, l2);
    expect(result).toEqual(expected);
  });

  // Test case: Both lists have one node and the sum is less than 10
  test("should return the sum of two nodes when both lists have one node", () => {
    let l1 = new ListNode(2);
    let l2 = new ListNode(3);
    let expected = new ListNode(5);
    let result = addTwoNumbers(l1, l2);
    expect(result).toEqual(expected);
  });

  // Test case: Both lists have one node and the sum is greater than or equal to 10
  test("should return the sum of two nodes with carry over", () => {
    let l1 = new ListNode(5);
    let l2 = new ListNode(7);
    let expected = new ListNode(2, new ListNode(1));
    let result = addTwoNumbers(l1, l2);
    expect(result).toEqual(expected);
  });

  // Test case: One list has more nodes than the other
  test("should return the sum of two lists with different lengths", () => {
    let l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    let l2 = new ListNode(5, new ListNode(6));
    let expected = new ListNode(7, new ListNode(0, new ListNode(4)));
    let result = addTwoNumbers(l1, l2);
    expect(result).toEqual(expected);
  });

  // Test case: Both lists have the same number of nodes with carry over
  test("should return the sum of two lists with carry over", () => {
    let l1 = new ListNode(9, new ListNode(9, new ListNode(9)));
    let l2 = new ListNode(1, new ListNode(1, new ListNode(1)));
    let expected = new ListNode(
      0,
      new ListNode(1, new ListNode(1, new ListNode(1)))
    );
    let result = addTwoNumbers(l1, l2);
    expect(result).toEqual(expected);
  });
});
