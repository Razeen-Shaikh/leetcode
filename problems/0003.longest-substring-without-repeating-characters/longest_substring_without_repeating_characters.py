"""
This module provides a solution for finding the length of
the longest substring in a given string without repeating characters.
"""

class Solution:
    """
    This class provides a solution for finding 
    the length of the longest substring in a given string without repeating characters.
    """
    def length_of_longest_substring(self, s: str) -> int:
        """
        Find the length of the longest substring in a given string without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        n = len(s)
        max_length = 0
        start = 0
        char_index_map = {}

        for end in range(n):
            # If the current character is already in the map
            # and its index is after the start of the current substring,
            # update the start of the substring to the next index of the repeated character.
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            # Update the index of the current character in the map.
            char_index_map[s[end]] = end
            # Update the maximum length if needed.
            max_length = max(max_length, end - start + 1)

        return max_length
