class Solution:
    def num_squares(self, n: int) -> int:
        # Create a list to store the least number of perfect squares that sum to each number from 0 to n
        dp = [0] * (n + 1)
        
        # Initialize the dp list
        for i in range(1, n + 1):
            dp[i] = i  # The maximum number of perfect squares needed for any number i is i itself
            
            # Try all possible perfect squares less than or equal to i
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], 1 + dp[i - j * j])
        
        return dp[n]
