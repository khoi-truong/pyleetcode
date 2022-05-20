"""
Unit tests for BFS problems
"""

from ..traverse import traverse
from ..tree_node import TreeNode


def test_traverse():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert traverse(root) == [[12], [7, 1], [9, 10, 5]]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert traverse(root) == [[1], [2, 3], [4, 5, 6, 7]]
