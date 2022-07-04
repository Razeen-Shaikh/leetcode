class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if(len(s) == 0):
            return True
        for c in t:
            if s[i] == c:
                i += 1
            if i == len(s):
                return True
