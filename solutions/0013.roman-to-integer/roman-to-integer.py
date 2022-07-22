class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        checked = False
        result = 0
        for i, c in enumerate(s):
            if (i < len(s) - 1) and ((c == "I" and s[i+1] == "V") or (c == "I" and s[i+1] == "X") or (c == "X" and s[i+1] == "L") or (c == "X" and s[i+1] == "C") or (c == "C" and s[i+1] == "D") or (c == "C" and s[i+1] == "M")):
                result += romanToInt[s[i+1]] - romanToInt[c]
                checked = True
            else: 
                if checked:
                    checked = False
                    continue
                checked = False
                result += romanToInt[c]
        return result
        