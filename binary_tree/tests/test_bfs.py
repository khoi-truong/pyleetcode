"""
Unit tests for BFS problems
"""

from typing import Optional

from ..bfs import (connect_all_siblings, connect_level_order_siblings,
                   find_level_averages, find_minimum_depth, find_successor,
                   level_order_traverse, reverse_level_order_traverse,
                   zigzag_level_order_traverse)
from ..tree_node import TreeNode


def get_mock_tree(number: int) -> Optional[TreeNode]:
    if number == 1:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        return root
    elif number == 2:
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        return root
    elif number == 3:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        return root
    elif number == 4:
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.left.right = TreeNode(2)
        return root
    elif number == 5:
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        return root


def test_level_order_traverse():
    assert not level_order_traverse(None)

    root = TreeNode(12)
    assert level_order_traverse(root) == [[12]]

    root = get_mock_tree(2)
    assert level_order_traverse(root) == [[12], [7, 1], [9, 10, 5]]

    root = get_mock_tree(1)
    assert level_order_traverse(root) == [[1], [2, 3], [4, 5, 6, 7]]


def test_reverse_level_order_traverse():
    assert not reverse_level_order_traverse(None)

    root = get_mock_tree(2)
    assert reverse_level_order_traverse(root) == [[9, 10, 5], [7, 1], [12]]

    root = get_mock_tree(1)
    assert reverse_level_order_traverse(root) == [[4, 5, 6, 7], [2, 3], [1]]


def test_zigzag_level_order_traverse():
    assert not zigzag_level_order_traverse(None)

    root = get_mock_tree(2)
    assert zigzag_level_order_traverse(root) == [[12], [1, 7], [9, 10, 5]]

    root = get_mock_tree(1)
    assert zigzag_level_order_traverse(root) == [[1], [3, 2], [4, 5, 6, 7]]


def test_find_level_averages():
    assert not find_level_averages(None)

    root = get_mock_tree(5)
    assert find_level_averages(root) == [12, 4, 6.5]

    root = get_mock_tree(1)
    assert find_level_averages(root) == [1, 2.5, 5.5]


def test_find_minimum_depth():
    assert not find_minimum_depth(None)

    root = get_mock_tree(4)
    assert find_minimum_depth(root) == 2

    root = get_mock_tree(1)
    assert find_minimum_depth(root) == 3


def test_find_successor():
    assert not find_successor(None, 1)

    root = get_mock_tree(3)
    result = find_successor(root, 3)
    assert result
    assert result.value == 4

    root = get_mock_tree(2)
    result = find_successor(root, 9)
    assert result
    assert result.value == 10


def test_connect_level_order_siblings():
    assert not connect_level_order_siblings(None)

    root = get_mock_tree(2)
    root = connect_level_order_siblings(root)
    assert root
    assert not root.next
    assert root.left and root.left.next
    assert root.left.next.value == 1
    assert root.right
    assert not root.right.next
    assert root.left.left and root.left.left.next
    assert root.left.left.next.value == 10
    assert root.right.left and root.right.left.next
    assert root.right.left.next.value == 5
    assert root.right.right
    assert not root.right.right.next


def test_connect_all_siblings():
    assert not connect_all_siblings(None)

    root = get_mock_tree(2)
    root = connect_all_siblings(root)
    assert root and root.next and root.next.value == 7
    assert root.next.next and root.next.next.value == 1
    assert root.next.next.next and root.next.next.next.value == 9
    assert root.next.next.next.next and root.next.next.next.next.value == 10
    assert root.next.next.next.next.next
    assert root.next.next.next.next.next.value == 5
    assert not root.next.next.next.next.next.next
