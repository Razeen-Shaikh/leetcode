from ast import List
from math import factorial


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(factorial(i)//(factorial(j)*factorial(i-j)))
            result.append(row)
        return result
