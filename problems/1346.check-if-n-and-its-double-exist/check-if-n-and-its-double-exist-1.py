from ast import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            rest_arr = arr[0:i]+arr[i+1:len(arr)]
            if 2 * arr[i] in rest_arr:
                return True
        
        return False