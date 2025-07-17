from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

        :param nums: A list of integers
        :param k: The number of most frequent elements to return
        :return: A list of the k most frequent elements
        """
        # Create a dictionary to store the frequency of each element
        frequency = {}

        # Count the frequency of each element
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Sort the dictionary by value in descending order
        sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

        # Return the k most frequent elements
        return list(sorted_frequency.keys())[:k]
