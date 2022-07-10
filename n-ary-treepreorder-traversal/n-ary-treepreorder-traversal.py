"""
# Definition for a Node.
"""


from ast import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)

        return result
