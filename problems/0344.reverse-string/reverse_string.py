"""
This module provides a solution for reversing a string in-place.
"""
from typing import List

class Solution:
    """
    This class provides a solution for reversing a string in-place.
    """
    def reverse_string(self, s: List[str]) -> None:
        """
        Reverses the input list of strings in-place.

        Args:
        s (List[str]): The list of strings to be reversed.

        Returns:
        None
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Swap characters at left and right indices
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
