"""
This module provides a solution to 
find the index of the first occurrence of a substring in a larger string.

The `Solution` class contains a method `str_str` that 
finds the index of the first occurrence of a substring in a larger string.
"""
class Solution:
    """
    This class represents a solution to a problem.
    It contains a method `strStr` that finds 
    the index of the first occurrence of a substring in a larger string.
    """
    def str_str(self, haystack: str, needle: str) -> int:
        """
        Find the index of the first occurrence of `needle` in `haystack`.

        Args:
            haystack (str): The input string to search in.
            needle (str): The substring to search for.

        Returns:
            int: The index of the first occurrence of `needle` in `haystack`,
            or -1 if `needle` is not found.
        """
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            sub_arr = haystack[i:i+m]
            if sub_arr == needle:
                return i
            if len(sub_arr) < m:
                return -1

        return -1
