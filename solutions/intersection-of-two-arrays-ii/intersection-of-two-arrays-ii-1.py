class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                nums.append(nums1[i])
        return nums
