"""
Problem: Best Time to Buy and Sell Stock
"""

import unittest
from src.sliding_window.best_time_to_buy_and_sell_stock import (
    BestTimeToBuyAndSellStockSlidingWindow,
    BestTimeToBuyAndSellStockSolution,
)


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    """
    Test cases for best time to buy and sell stock problem
    """

    def test_best_time_to_buy_and_sell_stock_sliding_window(self):
        sut = BestTimeToBuyAndSellStockSlidingWindow()
        self._test_best_time_to_buy_and_sell_stock(sut)

    def _test_best_time_to_buy_and_sell_stock(
        self,
        sut: BestTimeToBuyAndSellStockSolution,
    ):
        self.assertEqual(sut.max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(sut.max_profit([7, 6, 4, 3, 1]), 0)
