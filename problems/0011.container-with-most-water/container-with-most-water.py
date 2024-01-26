from ast import List


class Solution:
    """
    Class representing a solution for a specific problem.
    """
    def max_area(self, height: List[int]) -> int:
        """
        Calculate the maximum area of water that can be trapped between
        the vertical lines represented by the input list of heights.

        :param height: List of integers representing the heights of the vertical lines
        :return: Maximum area of water that can be trapped
        """
        max_water = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the current area
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            # Move pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
