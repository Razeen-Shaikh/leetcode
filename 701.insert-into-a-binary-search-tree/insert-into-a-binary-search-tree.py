# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node):
            if not node:
                return TreeNode(val, None, None)
            if node.val > val:
                if node.left:
                    insert(node.left)
                else:
                    node.left = TreeNode(val, None, None)
            else:
                if node.right:
                    insert(node.right)
                else:
                    node.right = TreeNode(val, None, None)
            return node
        return insert(root)
