# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        maxLevel = 1
        level = 1
        queue = collections.deque()
        queue.append(root)
        while queue:
            sum = 0
            currSize = len(queue)
            while currSize > 0:
                currNode = queue.popleft()
                sum += currNode.val
                currSize -= 1
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            if sum > maxSum:
                maxLevel = level
                maxSum = abs(sum)
            level += 1

        return maxLevel
