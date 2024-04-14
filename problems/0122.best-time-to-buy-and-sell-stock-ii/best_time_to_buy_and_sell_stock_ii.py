"""122. Best Time to Buy and Sell Stock II"""
from ast import List


class Solution:
    """
    Class to solve the Best Time to Buy and Sell Stock II problem.
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an integer array prices where prices[i] is 
        the price of a given stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. 
        You can only hold **at most one** share of the stock at any time. 
        However, you can buy it then immediately sell it on the **same day**.

        Find and return the maximum profit you can achieve.
        
        Args:
            prices (List[int]): A list of stock prices.
            
        Returns:
            int: The maximum profit that can be achieved.
        """
        max_profit = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                max_profit += profit
        return max_profit
