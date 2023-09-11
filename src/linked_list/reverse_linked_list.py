"""
Problem: Reverse Linked List
Leetcode: https://leetcode.com/problems/reverse-linked-list
"""

from abc import ABC, abstractmethod
from typing import Optional

from ..data_structures.list_node import ListNode


class ReverseLinkedListSolution(ABC):
    @abstractmethod
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


class ReverseLinkedListFirstSolution(ReverseLinkedListSolution):
    """
    First solution
    """

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
