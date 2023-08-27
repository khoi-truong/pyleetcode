"""
Problem: Linked List Cycle
"""

import unittest
from src.linked_list.list_node import ListNode
from src.linked_list.linked_list_cycle import (
    LinkedListCycleSolution,
    LinkedListCycleFastSlowPointers,
)


class TestLinkedListCycle(unittest.TestCase):
    """
    Test case for LinkedListCycle
    """

    def test_has_cycle_fast_and_slow_pointers(self):
        sut = LinkedListCycleFastSlowPointers()
        self._test_has_cycle(sut)

    def _test_has_cycle(self, sut: LinkedListCycleSolution):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head.next
        self.assertTrue(sut.has_cycle(head))

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head
        self.assertTrue(sut.has_cycle(head))

        head = ListNode(1)
        self.assertFalse(sut.has_cycle(head))
