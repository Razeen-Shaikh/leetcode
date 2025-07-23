from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.
        
        Args:
        nums (List[int]): The input array of integers.

        Returns:
        int: The length of the longest consecutive elements sequence.
        """
        if not nums:
            return 0

        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_sequence = max(longest_sequence, current_streak)

        return longest_sequence