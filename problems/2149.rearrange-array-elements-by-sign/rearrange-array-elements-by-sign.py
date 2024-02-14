"""
Module description: This module provides a solution for rearranging
elements in a list such that all positive numbers appear before all negative numbers.
"""
from typing import List

class Solution:
    """
    This class provides methods for rearranging elements in a
    list such that all positive numbers appear before all negative numbers.
    """
    def rearrange_array(self, nums: List[int]) -> List[int]:
        """
        Rearranges the elements in the given list such
        that all positive numbers appear before all negative numbers.
        
        Args:
            nums (List[int]): The list of integers to be rearranged.
        
        Returns:
            List[int]: The rearranged list of integers.
        """
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]

        result = []
        for pos, neg in zip(positives, negatives):
            result.append(pos)
            result.append(neg)

        return result
