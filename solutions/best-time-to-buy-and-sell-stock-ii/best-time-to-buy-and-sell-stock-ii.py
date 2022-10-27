from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if (profit > 0):
                max_profit += profit
        return max_profit
