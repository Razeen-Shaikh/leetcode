from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        freq = [0] * (size + 1)

        for row in grid:
            for num in row:
                freq[num] += 1

        repeated, missing = -1, -1

        for num in range(1, size + 1):
            if freq[num] == 2:
                repeated = num
            elif freq[num] == 0:
                missing = num

        return [repeated, missing]