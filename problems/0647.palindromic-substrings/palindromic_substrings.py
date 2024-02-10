"""Module to count palindromic substrings in a given string."""

class Solution:
    """
    This class provides methods for counting palindromic substrings in a given string.
    """
    def count_substrings(self, s: str) -> int:
        """
        Count the number of palindromic substrings in the given string.

        Args:
        s (str): The input string.

        Returns:
        int: The number of palindromic substrings.
        """
        n = len(s)
        count = 0
        # Initialize a 2D array to store whether substrings are palindromes
        dp = [[False] * n for _ in range(n)]

        # Single characters are always palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Check for substrings of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count
