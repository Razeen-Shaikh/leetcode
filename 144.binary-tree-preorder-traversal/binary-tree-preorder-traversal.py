# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def pot(node):
            if node is None:
                return None
            result.append(node.val)
            pot(node.left)
            pot(node.right)
        pot(root)
        return result
