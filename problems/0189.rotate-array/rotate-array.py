from ast import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums[len(nums)-1])
            del nums[len(nums)-1]
