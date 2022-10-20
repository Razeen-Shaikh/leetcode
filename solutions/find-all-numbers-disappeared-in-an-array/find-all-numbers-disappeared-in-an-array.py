from ast import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = [num for num in range(1, len(nums)+1)]
        return list(set(temp) - set(nums))
