"""
Problem: Min Stack
"""

import unittest
from src.stack.min_stack import MinStack


class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        sut = MinStack()
        sut.push(-2)
        sut.push(0)
        sut.push(-3)
        self.assertEqual(sut.get_min(), -3)
        sut.pop()
        self.assertEqual(sut.top(), 0)
        self.assertEqual(sut.get_min(), -2)
