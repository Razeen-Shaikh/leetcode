from ast import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        count = 0
        for i in range(len(arr)):
            if (arr[i] == 0):
                count += 1
            elif ((2 * arr[i]) in arr):
                return True
        if (count > 1):
            return True
        return False
