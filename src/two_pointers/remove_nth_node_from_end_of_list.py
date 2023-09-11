"""
Problem: Remove Nth Node From End of List
Leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""

from abc import ABC, abstractmethod
from typing import Optional
from ..data_structures.list_node import ListNode


class Solution(ABC):
    @abstractmethod
    def remove_nth_from_end(self, head: ListNode, n: int) -> Optional[ListNode]:
        pass


class TwoPointersSolution(Solution):
    """
    Solution: Two Pointers
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def remove_nth_from_end(self, head: ListNode, n: int) -> Optional[ListNode]:
        start = ListNode()
        start.next = head
        left = start
        right = start
        for _ in range(n):
            if right.next:
                right = right.next
            else:
                return head
        while left and right and right.next:
            left = left.next
            right = right.next
        if left and left.next:
            left.next = left.next.next
        return start.next
