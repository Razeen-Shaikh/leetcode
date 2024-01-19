from ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        duplicates = [x for i, x in enumerate(nums) if x in nums[:i]]
        non_duplicates = list(set(nums))
        for i in range(len(non_duplicates)):
            if non_duplicates[i] not in duplicates:
                return non_duplicates[i]
