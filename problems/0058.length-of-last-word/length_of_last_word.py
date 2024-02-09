"""
This module provides a solution for finding the length of the last word in a given input string.
"""

class Solution:
    """
    This class provides a solution for finding the length of the last word in a given input string.
    """
    def length_of_last_word(self, s: str) -> int:
        """
        Returns the length of the last word in
        the input string after stripping whitespace from the ends.
        
        Args:
        s (str): The input string
        
        Returns:
        int: The length of the last word
        """
        s = s.strip()
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return length
            length += 1
        return length
