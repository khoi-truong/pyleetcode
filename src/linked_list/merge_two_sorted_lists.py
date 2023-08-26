"""
Problem: Merge Two Sorted Lists
Leetcode: https://leetcode.com/problems/merge-two-sorted-lists
"""


from abc import ABC, abstractmethod
from typing import Optional
from .list_node import ListNode


class MergeTwoSortedListsSolution(ABC):
    @abstractmethod
    def merge_two_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        pass


class MergeTwoSortedListFistSolution(MergeTwoSortedListsSolution):
    """
    Merge two sorted linked lists and return it as a new sorted list.

    Parameters:
        list1 (Optional[ListNode]): The head of the first linked list.
        list2 (Optional[ListNode]): The head of the second linked list.

    Returns:
        Optional[ListNode]: The head of the merged sorted linked list.
    """

    def merge_two_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        result = ListNode()
        current = result
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return result.next
