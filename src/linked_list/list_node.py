"""
ListNode - Definition for singly-linked list.
"""

from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val: int = 0):
        self.val = val
        self.next: Optional[ListNode] = None
