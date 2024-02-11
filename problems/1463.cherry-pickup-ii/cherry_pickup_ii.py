"""
Module providing a solution for the cherry pickup problem.
"""
from typing import List

class Solution:
    """
    This class provides a solution for cherry pickup problem.
    """
    def cherry_pickup(self, grid: List[List[int]]) -> int:
        """
        Calculate the maximum cherries that can be collected by two robots moving simultaneously from the top-left to the bottom-right of the grid.
        
        Args:
        grid (List[List[int]]): The grid representing the cherries at each cell
        
        Returns:
        int: The maximum number of cherries that can be collected
        """
        rows, cols = len(grid), len(grid[0])

        # Initialize a 3-dimensional array to store the maximum cherries collected
        # dp[i][j][k] represents the maximum cherries collected up to row i,
        # with robot1 at column j and robot2 at column k
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]

        def collect_cherries(row, col1, col2):
            # Compute the cherries collected by both robots in the current cell
            cherries = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            return cherries

        def max_cherries(row, col1, col2):
            # If we have reached the bottom row, return 0
            if row == rows:
                return 0

            # If we have already computed the result for this state, return it
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]

            # Initialize the maximum cherries collected from the current state
            max_cherries = 0

            # Iterate through possible next states for both robots
            for next_col1 in range(col1 - 1, col1 + 2):
                for next_col2 in range(col2 - 1, col2 + 2):
                    # Check if both next states are within the grid
                    if 0 <= next_col1 < cols and 0 <= next_col2 < cols:
                        # Recursively compute the maximum cherries collected from the next state
                        max_cherries = max(max_cherries, dfs(row + 1, next_col1, next_col2))

            # Update the result for the current state and return it
            dp[row][col1][col2] = max_cherries + collect_cherries(row, col1, col2)
            return dp[row][col1][col2]

        # Start the recursion from the top row with both robots at the top row
        def dfs(row, col1, col2):
            return max_cherries(row, col1, col2)

        return dfs(0, 0, cols - 1)
