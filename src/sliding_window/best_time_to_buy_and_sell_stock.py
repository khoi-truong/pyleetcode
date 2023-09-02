"""
Problem: Best Time to Buy and Sell Stock
Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from abc import ABC, abstractmethod


class BestTimeToBuyAndSellStockSolution(ABC):
    @abstractmethod
    def max_profit(self, prices: list[int]) -> int:
        """
        Returns the max profit that can be made from buying and selling stocks.
        """
        pass


class BestTimeToBuyAndSellStockSlidingWindow(BestTimeToBuyAndSellStockSolution):
    def max_profit(self, prices: list[int]) -> int:
        result = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            result = max(result, price - lowest)
        return result
