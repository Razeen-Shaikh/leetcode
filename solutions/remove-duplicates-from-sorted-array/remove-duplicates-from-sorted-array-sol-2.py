from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums.copy()
        for index, num in enumerate(temp):
            if (index != temp.index(num)):
                nums.remove(num)
        return len(nums)
