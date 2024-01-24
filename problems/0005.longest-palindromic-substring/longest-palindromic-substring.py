class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # Create a table to store the results of subproblems
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        start, max_length = 0, 1  # Initialize the start index and maximum length

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # Check substrings of length 3 and above
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the substring

                # Check if the substring is a palindrome
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        # Return the longest palindromic substring
        return s[start:start + max_length]

