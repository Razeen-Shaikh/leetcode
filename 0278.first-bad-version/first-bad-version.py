# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l < r:
            midElem = (l + r) // 2
            if isBadVersion(midElem):
                r = midElem
            else:
                l = midElem + 1

        if r == l and isBadVersion(l):
            return l

        return -1
