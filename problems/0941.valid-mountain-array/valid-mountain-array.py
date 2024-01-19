from ast import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) < 3):
            return False
        first_half = arr[0:arr.index(max(arr))]
        first_half_dupes = [x for i, x in enumerate(
            first_half) if x in first_half[:i]]
        sec_half = arr[arr.index(max(arr))+1:len(arr)]
        sec_half_dupes = [x for i, x in enumerate(
            sec_half) if x in sec_half[:i]]
        return first_half and sec_half and not (first_half_dupes or sec_half_dupes) and max(arr) not in first_half and max(arr) not in sec_half and sorted(first_half) == first_half and sorted(sec_half, reverse=True) == sec_half
