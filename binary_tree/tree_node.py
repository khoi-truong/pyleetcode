"""
Node of a binary tree
"""
from typing import Optional


class TreeNode:
    """
    Node of a binary tree
    """

    def __init__(self,
                 value: int,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None,
                 nekt: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = nekt

    # level order traversal using 'next' pointer
    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.value) + " ", end="")
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()
