# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return None
            temp = node.left
            node.left = node.right
            node.right = temp
            invert(node.left)
            invert(node.right)

            return node

        return invert(root)
