from ast import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers `nums` and an integer `target`, 
        return indices of the two numbers such that they add up to `target`.
        You may assume that each input would have **_exactly one solution_**,
        and you may not use the same element twice.
        
        Args:
            nums: A list of integers.
            target: The target sum.
            
        Returns:
            A list of two integers,
            representing the indices of the two numbers that add up to the target.
        """
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], i]

            num_indices[num] = i

        return []