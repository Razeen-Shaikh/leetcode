"""
Module for finding the least number of unique
integers after removing k elements from the input array.
"""
from collections import Counter
from typing import List

class Solution:
    """
    Class for finding the least number of unique
    integers after removing k elements from the input array.
    """
    def find_least_num_of_unique_ints(self, arr: List[int], k: int) -> int:
        """
        Finds the least number of unique integers after removing k elements from the input array.

        Args:
            arr (List[int]): The input array of integers
            k (int): The number of elements to remove

        Returns:
            int: The least number of unique integers after removing k elements
        """
        frequency = Counter(arr)

        sorted_freq = sorted(frequency.values())

        unique_count = len(sorted_freq)

        for freq in sorted_freq:
            if k >= freq:
                k -= freq
                unique_count -= 1
            else:
                break

        return unique_count
