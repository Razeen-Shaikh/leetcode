class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = s
        for i, c in enumerate(s):
            if i != s.index(c):
                t = t.replace(s[i], "")
        if len(t) > 0:
            return s.index(t[0])
        else:
            return -1
