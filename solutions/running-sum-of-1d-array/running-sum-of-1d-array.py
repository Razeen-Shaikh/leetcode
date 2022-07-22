from ast import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        for i in range(len(nums)):
            sums.append(sum(nums[0:i+1]))
        return sums
