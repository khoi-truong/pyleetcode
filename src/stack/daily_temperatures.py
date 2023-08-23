"""
Problem: Daily Temperatures
Leetcode: https://leetcode.com/problems/daily-temperatures/
"""

from abc import ABC, abstractmethod


class DailyTemperaturesSolution(ABC):
    """
    Abstract base class for Daily Temperatures solution
    """

    @abstractmethod
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        pass


class DailyTemperaturesStack(DailyTemperaturesSolution):
    """
    Solution: Monotonic Stack
    Reference: https://youtu.be/Dq_ObZwTY_Q
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = list[tuple[int, int]]()
        for current_index, current in enumerate(temperatures):
            while stack and current > stack[-1][0]:
                _, index = stack.pop()
                result[index] = current_index - index
            stack.append((current, current_index))
        return result
