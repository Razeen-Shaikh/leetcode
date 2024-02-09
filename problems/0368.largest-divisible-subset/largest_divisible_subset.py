""" Module to find the largest divisible subset of a given list of integers. """
from typing import List

class Solution:
    """
    This class provides methods for finding
    the largest divisible subset of a given list of integers.
    """
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        """
        Finds the largest divisible subset of the given list of integers.

        Args:
            nums: A list of integers from which the largest divisible subset needs to be found.

        Returns:
            A list of integers representing the largest divisible subset.
        """
        if not nums:
            return []

        nums.sort()
        dp = [[num] for num in nums]

        for i, num in enumerate(nums):
            for j in range(i):
                if num % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [num]

        return max(dp, key=len)
