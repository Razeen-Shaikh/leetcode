from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = nums1+nums2
        mergedArray.sort()
        median = 0
        if len(mergedArray) % 2 == 0:
            median = (mergedArray[int(len(mergedArray)/2)] +
                      mergedArray[int(len(mergedArray)/2)-1])/2
        else:
            median = mergedArray[int(len(mergedArray)/2)]
        return median
