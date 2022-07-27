from ast import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def square(x): return x*x
        snums = list(map(square, nums))
        snums.sort()
        return snums
