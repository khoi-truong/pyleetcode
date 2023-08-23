"""
Problem: Daily Temperatures
"""

import unittest
from src.stack.daily_temperatures import (
    DailyTemperaturesStack,
    DailyTemperaturesSolution,
)


class TestDailyTemperature(unittest.TestCase):
    """
    Test cases for Daily Temperatures
    """

    def test_daily_temperatures_stack(self):
        sut = DailyTemperaturesStack()
        self._test_daily_temperatures(sut)

    def _test_daily_temperatures(self, sut: DailyTemperaturesSolution):
        self.assertCountEqual(
            sut.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertEqual(
            sut.daily_temperatures([30, 40, 50, 60]),
            [1, 1, 1, 0],
        )
        self.assertEqual(
            sut.daily_temperatures([30, 60, 90]),
            [1, 1, 0],
        )
