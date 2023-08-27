"""
Problem: Linked List Cycle
Leetcode: https://leetcode.com/problems/linked-list-cycle
"""


from abc import ABC, abstractmethod
from typing import Optional
from .list_node import ListNode


class LinkedListCycleSolution(ABC):
    @abstractmethod
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        pass


class LinkedListCycleFastSlowPointers(LinkedListCycleSolution):
    """
    Solution: Fast and Slow Pointers
    Time Complexity: O(n)
    """

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head
        slow = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
