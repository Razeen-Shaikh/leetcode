class Solution:
    def isPalindrome(self, x: int) -> bool:
        xlist = [i for i in str(x)]
        return xlist == xlist[::-1]
