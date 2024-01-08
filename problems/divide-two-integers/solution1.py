class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(int(dividend/divisor) > 2147483647): return 2147483647
        return int(dividend/divisor)