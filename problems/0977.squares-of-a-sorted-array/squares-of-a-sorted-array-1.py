from ast import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrNums = list(map(lambda x: x*x, nums))
        return sorted(sqrNums)
