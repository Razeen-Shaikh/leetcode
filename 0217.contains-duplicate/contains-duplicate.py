from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return nums != list(dict.fromkeys(nums))
