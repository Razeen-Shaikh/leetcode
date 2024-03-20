"""
Module to calculate the furthest building that can be reached using the given bricks and ladders.
"""
import heapq
from typing import List

class Solution:
    """
    Class to calculate the furthest building that can be reached using the given bricks and ladders.
    """
    def furthest_building(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Calculate the furthest building that can be reached using the given bricks and ladders.

        Args:
            heights (List[int]): List of heights of the buildings
            bricks (int): Number of bricks available
            ladders (int): Number of ladders available

        Returns:
            int: Index of the furthest reachable building
        """
        pq = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(pq, diff)
                if len(pq) > ladders:
                    bricks -= heapq.heappop(pq)
                if bricks < 0:
                    return i
        return len(heights) - 1
