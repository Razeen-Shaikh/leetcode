from itertools import permutations
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()

        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            number = perm[0]*100 + perm[1]*10 + perm[2]
            if number % 2 == 0:
                result.add(number)

        return sorted(result)