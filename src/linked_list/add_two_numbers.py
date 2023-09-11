"""
Problem: Add Two Numbers
Leetcode: https://leetcode.com/problems/add-two-numbers
"""

from abc import ABC, abstractmethod
from typing import Optional
from ..data_structures.list_node import ListNode


class AddTwoNumbersSolution(ABC):
    @abstractmethod
    def add_two_numbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        pass


class AddTwoNumbersFirstSolution(AddTwoNumbersSolution):
    """
    Solution: Singly Linked List
    Time Complexity: O(n)
    """

    def add_two_numbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        result = ListNode()
        current = result
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return result.next
