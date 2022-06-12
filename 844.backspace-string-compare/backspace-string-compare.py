class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        backspace = "#"
        newS = ""
        newT = ""
        for i in range(len(s)):
            if s[i] != backspace:
                newS += s[i]
            else:
                newS = newS[:len(newS)-1]
        for j in range(len(t)):
            if t[j] != backspace:
                newT += t[j]
            else:
                newT = newT[:len(newT)-1]

        return newS == newT
