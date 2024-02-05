from typing import List

class Solution:
    """
    This class provides a solution for finding the closest sum of three integers in the given list to the target value.
    """
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """
        Finds the closest sum of three integers in the given list to the target value.

        Args:
        - nums (List[int]): The input list of integers.
        - target (int): The target value.

        Returns:
        - int: The closest sum of three integers to the target value.
        """
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update the closest sum
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Adjust pointers based on the current sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the sum is equal to the target, return the sum
                    return closest_sum

        return closest_sum
