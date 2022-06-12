/**
 * 700. Search in a Binary Search Tree
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function (root, val) {
	let res = null;
	if (!root || root.val === val) return root;
	else {
		if (root && root.val < val) return searchBST(root.right, val);
		return searchBST(root.left, val);
	}
};
