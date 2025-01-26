from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
        
        Args:
        prices (List[int]): An array where prices[i] is the price of a given stock on the ith day.
        
        Returns:
        int: The maximum profit you can achieve from this transaction.
        """
        l = 0
        r = 1
        currMax = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                currMax = max(currMax, profit)
            else:
                l = r
            r += 1

        return currMax
