"""
Module description: This module contains a Solution
class with methods for finding palindromes in a list of words.
"""

from ast import List

class Solution:
    """
    This class provides methods for finding palindromes in a list of words.
    """
    def first_palindrome(self, words: List[str]) -> str:
        """
        Finds the first palindrome in the list of words.

        Args:
        - words: List of strings

        Returns:
        - The first palindrome found in the list, or an empty string if none is found.
        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""
