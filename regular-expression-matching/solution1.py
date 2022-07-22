class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if "*" not in p and "." not in p:
            if(s == p):
                return True
            return False

        def match(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            m = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                return match(i, j+2) or (m and match(i + 1, j))

            if m:
                return match(i+1, j+1)
            return False
        return match(0, 0)
