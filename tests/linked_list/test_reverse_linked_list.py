"""
Problem: Reverse Linked List
"""

import unittest
from src.linked_list.reverse_linked_list import (
    ReverseLinkedListSolution,
    ReverseLinkedListFirstSolution,
)
from src.data_structures.list_node import ListNode


class TestReverseLinkedList(unittest.TestCase):
    """
    Test case for ReverseLinkedList
    """

    def test_reverse_linked_list_first_solution(self):
        sut = ReverseLinkedListFirstSolution()
        self._test_reverse_linked_list(sut)

    def _test_reverse_linked_list(self, sut: ReverseLinkedListSolution):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        result = sut.reverse_list(head)
        self.assertEqual(result.val, 5)  # type: ignore
        self.assertEqual(result.next.val, 4)  # type: ignore
        self.assertEqual(result.next.next.val, 3)  # type: ignore
        self.assertEqual(result.next.next.next.val, 2)  # type: ignore
        self.assertEqual(result.next.next.next.next.val, 1)  # type: ignore
