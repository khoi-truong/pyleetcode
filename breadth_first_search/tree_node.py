"""
Node of a binary tree
"""
from typing import Optional


class TreeNode:

    def __init__(self, value):
        self.value: int = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
