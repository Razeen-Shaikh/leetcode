from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = [0, 0]
        if target in nums:
            index[0] = nums.index(target)
        else:
            return [-1, -1]
        for i, num in reversed(list(enumerate(nums))):
            if num == target:
                index[1] = i
                break
        return index
