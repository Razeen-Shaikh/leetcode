"""Two Sums"""

from ast import List

class Solution:
    """
    Class to provide solutions for specific problems.
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Find the indices of the two numbers in the list 'nums' that add up to the 'target'.
        
        Args:
            nums: A list of integers.
            target: The target sum.
            
        Returns:
            A list of two integers,
            representing the indices of the two numbers that add up to the target.
        """
        num_indices = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_indices:
                # Return the indices of the two numbers that add up to the target
                return [num_indices[complement], i]

            # Add the current number and its index to the dictionary
            num_indices[num] = i

        # If no solution is found, return an empty list
        # (this should not happen based on the problem statement)
        return []