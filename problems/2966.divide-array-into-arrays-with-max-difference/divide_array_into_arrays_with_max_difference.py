"""
Module description goes here
"""
from ast import List


class Solution:
    """
    This class provides a solution for dividing the input array into sub_arrays of size k.
    """
    def divide_array(self, numbers: List[int], k: int) -> List[List[int]]:
        """
        Divide the input array into sub_arrays of size k, and return a list of sub_arrays.
        
        Args:
            numbers (List[int]): The input array of integers.
            k (int): The size of the sub_arrays.

        Returns:
            List[List[int]]: A list of sub_arrays.

        Example:
            >>> s = Solution()
            >>> s.divideArray([1, 2, 3, 4, 5], 2)
            [[1, 2], [3, 4], [5]]
        """
        n = len(numbers)
        result = []

        # Sort the array to simplify the process
        numbers.sort()

        # Iterate through the sorted array
        i = 0
        while i < n:
            current_array = []

            # Construct a sub_array of size 3
            for j in range(3):
                if i < n:
                    current_array.append(numbers[i])
                    i += 1
                else:
                    break

            # Check the conditions for the constructed sub_array
            if len(current_array) == 3 and current_array[2] - current_array[0] <= k:
                result.append(current_array)
            else:
                # If conditions are not met, return an empty array
                return []

        return result
