# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        while res:
            if p.val > res.val and q.val > res.val:
                res = res.right
            elif p.val < res.val and q.val < res.val:
                res = res.left
            else:
                return res
