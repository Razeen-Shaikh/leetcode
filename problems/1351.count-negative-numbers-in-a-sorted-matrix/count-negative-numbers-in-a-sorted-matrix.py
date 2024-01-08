from ast import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for l in grid:
            for i in range(len(l)-1, -1, -1):
                if l[i] >= 0:
                    break
                count += 1
        return count
