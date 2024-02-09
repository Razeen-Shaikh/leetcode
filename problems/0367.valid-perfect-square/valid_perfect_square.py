from cmath import sqrt
from math import floor


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(floor(sqrt(num)) == sqrt(num)):
            return True
