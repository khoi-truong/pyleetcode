"""
Unit tests for BFS problems
"""

from ..traverse import (find_level_averages, find_minimum_depth,
                        level_order_traverse, reverse_level_order_traverse,
                        zigzag_level_order_traverse)
from ..tree_node import TreeNode


def test_level_order_traverse():
    assert not level_order_traverse(None)

    root = TreeNode(12)
    assert level_order_traverse(root) == [[12]]

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert level_order_traverse(root) == [[12], [7, 1], [9, 10, 5]]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert level_order_traverse(root) == [[1], [2, 3], [4, 5, 6, 7]]


def test_reverse_level_order_traverse():
    assert not reverse_level_order_traverse(None)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert reverse_level_order_traverse(root) == [[9, 10, 5], [7, 1], [12]]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert reverse_level_order_traverse(root) == [[4, 5, 6, 7], [2, 3], [1]]


def test_zigzag_level_order_traverse():
    assert not zigzag_level_order_traverse(None)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert zigzag_level_order_traverse(root) == [[12], [1, 7], [9, 10, 5]]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert zigzag_level_order_traverse(root) == [[1], [3, 2], [4, 5, 6, 7]]


def test_find_level_averages():
    assert not find_level_averages(None)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert find_level_averages(root) == [12, 4, 6.5]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert find_level_averages(root) == [1, 2.5, 5.5]


def test_find_minimum_depth():
    assert not find_minimum_depth(None)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    assert find_minimum_depth(root) == 2

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert find_minimum_depth(root) == 3
