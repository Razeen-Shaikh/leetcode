from ast import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
