# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def printInOrder(node):
            if node is None:
                return None
            printInOrder(node.left)
            result.append(node.val)
            printInOrder(node.right)

        printInOrder(root)
        return result
