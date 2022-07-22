from ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if maxOnes < count:
                    maxOnes = count
                count = 0
        if maxOnes < count:
            maxOnes = count
        return maxOnes
