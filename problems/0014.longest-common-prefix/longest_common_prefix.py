"""
Module to perform operations related to finding
the longest common prefix among a list of strings.
"""
from ast import List


class Solution:
    """
    Class to perform operations related to finding
    the longest common prefix among a list of strings.
    """
    def longest_common_prefix(self, strings: List[str]) -> str:
        """
        Find the longest common prefix among a list of strings.

        Args:
        - strings: List of strings to find the common prefix from

        Returns:
        - The longest common prefix string
        """
        if not strings:
            return ""

        # Sort the strings to make it easier to find the common prefix
        strings.sort()

        # Take the first and last strings in the sorted array
        first_str = strings[0]
        last_str = strings[-1]

        # Find the common prefix character by character
        common_prefix = ""
        for i, char in enumerate(first_str):
            if i < len(last_str) and char == last_str[i]:
                common_prefix += char
            else:
                break

        return common_prefix
