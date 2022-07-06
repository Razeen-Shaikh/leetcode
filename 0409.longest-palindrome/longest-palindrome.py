class Solution:
    def longestPalindrome(self, s: str) -> int:
        occ = {}
        length = 0
        for i, c in enumerate(s):
            if c in occ:
                occ[c] += 1
            else:
                occ[c] = 1

        for o in occ:
            length += occ[o] // 2 * 2
            if length % 2 == 0 and occ[o] % 2 == 1:
                length += 1

        return length
