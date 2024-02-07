"""
Module description: This module provides methods for sorting input strings based on character frequencies.
"""

class Solution:
    """
    A class that provides methods for sorting input strings based on character frequencies.
    """
    def frequency_sort(self, s: str) -> str:
        """
        Sorts the input string based on character frequencies in decreasing order.

        Args:
        s (str): The input string to be sorted.

        Returns:
        str: The sorted string based on character frequencies.
        """
        # Step 1: Count the frequency of each character
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Step 2: Sort characters based on their frequencies in decreasing order
        sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)
        
        # Step 3: Construct the sorted string
        sorted_string = ''.join(char * char_freq[char] for char in sorted_chars)
        
        return sorted_string
