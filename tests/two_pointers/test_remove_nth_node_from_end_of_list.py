"""
Problem: Remove Nth Node From End of List
"""

import unittest
from src.data_structures.list_node import ListNode
from src.two_pointers.remove_nth_node_from_end_of_list import (
    Solution,
    TwoPointersSolution,
)


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):
    """
    Test case for Remove Nth Node From End of List
    """

    def test_two_pointers_solution(self) -> None:
        sut = TwoPointersSolution()
        self._test_solution(sut)

    def _test_solution(self, sut: Solution) -> None:
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        result = sut.remove_nth_from_end(head, 2)
        self.assertEqual(result.val, 1)  # type: ignore
        self.assertEqual(result.next.val, 2)  # type: ignore
        self.assertEqual(result.next.next.val, 3)  # type: ignore
        self.assertEqual(result.next.next.next.val, 5)  # type: ignore
        self.assertIsNone(result.next.next.next.next)  # type: ignore

        head = ListNode(1)
        result = sut.remove_nth_from_end(head, 1)
        self.assertIsNone(result)

        head = ListNode(1)
        head.next = ListNode(2)
        result = sut.remove_nth_from_end(head, 1)
        self.assertEqual(result.val, 1)  # type: ignore
        self.assertIsNone(result.next)  # type: ignore
