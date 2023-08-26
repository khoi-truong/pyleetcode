"""
Problem: Add Two Numbers
"""

import unittest
from src.linked_list.list_node import ListNode
from src.linked_list.add_two_numbers import (
    AddTwoNumbersFirstSolution,
    AddTwoNumbersSolution,
)


class TestAddTwoNumbers(unittest.TestCase):
    """
    Test case for AddTwoNumbers
    """

    def test_add_two_numbers_fist_solution(self):
        sut = AddTwoNumbersFirstSolution()
        self._test_add_two_numbers(sut)

    def _test_add_two_numbers(self, sut: AddTwoNumbersSolution):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        result = sut.add_two_numbers(l1, l2)
        self.assertEqual(result.val, 7)  # type: ignore
        self.assertEqual(result.next.val, 0)  # type: ignore
        self.assertEqual(result.next.next.val, 8)  # type: ignore

        l1 = ListNode(0)
        l2 = ListNode(0)
        result = sut.add_two_numbers(l1, l2)
        self.assertEqual(result.val, 0)  # type: ignore

        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)
        l1.next.next.next = ListNode(9)
        l1.next.next.next.next = ListNode(9)
        l1.next.next.next.next.next = ListNode(9)
        l1.next.next.next.next.next.next = ListNode(9)
        l2 = ListNode(9)
        l2.next = ListNode(9)
        l2.next.next = ListNode(9)
        l2.next.next.next = ListNode(9)
        result = sut.add_two_numbers(l1, l2)
        self.assertEqual(result.val, 8)  # type: ignore
        self.assertEqual(result.next.val, 9)  # type: ignore
        self.assertEqual(result.next.next.val, 9)  # type: ignore
        self.assertEqual(result.next.next.next.val, 9)  # type: ignore
        self.assertEqual(result.next.next.next.next.val, 0)  # type: ignore
        self.assertEqual(result.next.next.next.next.next.val, 0)  # type: ignore
        self.assertEqual(result.next.next.next.next.next.next.val, 0)  # type: ignore
        self.assertEqual(
            result.next.next.next.next.next.next.next.val,  # type: ignore
            1,
        )
