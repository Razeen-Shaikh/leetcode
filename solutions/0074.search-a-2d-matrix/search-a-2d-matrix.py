from ast import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target <= 10**4:
            for mlist in matrix:
                maxNum = max(mlist)
                if(maxNum == target):
                    return True
                elif target > maxNum:
                    continue
                else:
                    return (target in mlist)
