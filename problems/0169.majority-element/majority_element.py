"""
Module to perform majority element calculation.
"""
from typing import List

class Solution:
    """
    Class to perform majority element calculation.
    """
    def majority_element(self, nums: List[int]) -> int:
        """
        Find the majority element in a given list of integers.

        Args:
        - nums: List of integers

        Returns:
        - The majority element
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
