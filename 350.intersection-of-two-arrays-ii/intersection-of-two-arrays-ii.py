from ast import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if (len(nums1) >= 1) and (len(nums2) <= 1000):
            if len(nums1) < len(nums2):
                snums = nums1
                lnums = nums2
            else:
                snums = nums2
                lnums = nums1

            print(snums, lnums)
            for i, num in enumerate(snums):
                if num in lnums:
                    res.append(num)
                    lnums.remove(num)
        return res
