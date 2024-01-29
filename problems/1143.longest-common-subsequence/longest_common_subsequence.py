"""
This module provides a solution for finding the length of 
the longest common subsequence between two input strings.
"""
class Solution:
    """
    Class for finding the length of the longest common subsequence between two input strings.
    """
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Finds the length of the longest common subsequence between text1 and text2.

        Args:
            text1 (str): The first input string.
            text2 (str): The second input string.

        Returns:
            int: The length of the longest common subsequence.
        """
        m = len(text1)
        n = len(text2)

        # Initialize a 2D array to store the lengths of common subsequences
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp array based on the characters in text1 and text2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The result is stored in the bottom-right cell of the dp array
        return dp[m][n]
