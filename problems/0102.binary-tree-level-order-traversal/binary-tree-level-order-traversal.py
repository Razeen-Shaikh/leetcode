# Definition for a binary tree node.
from ast import List
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queueSize = len(queue)
            levelList = []

            while queueSize > 0:
                node = queue.popleft()
                levelList.append(node.val)
                queueSize -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(levelList)

        return result
