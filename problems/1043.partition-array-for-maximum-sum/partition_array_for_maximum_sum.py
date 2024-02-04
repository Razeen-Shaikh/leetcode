"""
Module description: This module provides a solution for the max_sum_after_partitioning problem.
"""
from ast import List


class Solution:
    """
    This class provides a solution for the max_sum_after_partitioning problem.
    """
    def max_sum_after_partitioning(self, arr: List[int], k: int) -> int:
        """
        Calculate the maximum sum after partitioning the input array.

        Args:
        arr (List[int]): The input array.
        k (int): The maximum length of each partition.

        Returns:
        int: The maximum sum after partitioning the array.
        """
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            max_val = float('-inf')
            for j in range(1, min(k, i + 1) + 1):
                max_val = max(max_val, arr[i - j + 1])
                dp[i] = max(dp[i], (dp[i - j] if i - j >= 0 else 0) + max_val * j)

        return dp[-1]
