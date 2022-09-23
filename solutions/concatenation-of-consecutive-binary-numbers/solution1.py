class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaryStr = ""
        for i in range(1,n+1):
            binaryStr += str(bin(i).replace("0b", ""))
        return int(binaryStr, 2) % (10**9 + 7)