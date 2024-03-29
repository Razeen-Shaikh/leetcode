"""
Module description: This module provides methods
for checking if two strings are anagrams of each other.
"""
class Solution:
    """
    This class provides methods for checking if two strings are anagrams of each other.
    """
    def is_anagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.

        Args:
        - s (str): The first input string.
        - t (str): The second input string.

        Returns:
        - bool: True if the strings are anagrams, False otherwise.
        """
        if("".join(sorted(s.lower())) == "".join(sorted(t.lower()))):
            return True
