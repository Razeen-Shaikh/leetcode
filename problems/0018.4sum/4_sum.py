"""
This module provides a solution for finding unique
quadruplets in a list of numbers that sum up to a target value.
"""
from typing import List

class Solution:
    """
    This class provides methods for finding unique
    quadruplets in a list of numbers that sum up to a target value.
    """
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique quadruplets in the list of numbers 'nums' that sum up to the target value.
        
        Args:
            - nums: A list of integers
            - target: The target sum
            
        Returns:
            - A list of lists, each representing a unique quadruplet that sums up to the target
        """
        nums.sort()
        quadruplets = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets
