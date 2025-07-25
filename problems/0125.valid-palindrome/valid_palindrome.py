"""125 Valid Palindrome"""

import re

class Solution:
    """
    This class provides methods for checking palindromes in strings.
    """
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
        and removing all non-alphanumeric characters, it reads the same forward and backward. 
        Alphanumeric characters include letters and numbers.
        Given a string s, return true if it is a palindrome, or false otherwise.

        Parameters:
        s (str): The input string to check for palindrome.

        Returns:
        bool: True if the input string is a palindrome, False otherwise.
        """
        matches = re.findall(r'[a-zA-Z\d]', s)
        sentence = ''.join(matches).lower()
        reverse_str = "".join(sentence[i] for i in range(len(sentence)-1, -1, -1))
        return reverse_str == sentence
