class Solution:
    def reverse(self, x: int) -> int:
        rev = []
        if x < 0:
            intToList = [i for i in str(abs(x))]
            rev = ["-"]
            rev.append("".join(intToList[::-1]))
            rev = int("".join(rev))
        else:
            intToList = [i for i in str(x)]
            rev = int("".join(intToList[::-1]))
        if (rev >= (-(2**31))) and (rev <= (2**31 - 1)):
            return rev
        return 0
