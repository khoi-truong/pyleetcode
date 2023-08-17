"""
Unit tests for BFS problems
"""
from binary_tree.bfs import (
    connect_all_siblings,
    connect_level_order_siblings,
    find_level_averages,
    find_minimum_depth,
    find_successor,
    level_order_traverse,
    reverse_level_order_traverse,
    zigzag_level_order_traverse,
)
from binary_tree.tree_node import TreeNode as Node


def get_mock_tree(number: int = 0) -> Node:
    if number == 1:
        return Node(12, Node(7, Node(9)), Node(1, Node(10), Node(5)))
    elif number == 2:
        return Node(1, Node(2, Node(4), Node(5)), Node(3))
    elif number == 3:
        return Node(12, Node(7, Node(9), Node(2)), Node(1))
    elif number == 4:
        return Node(12, Node(7, Node(9), Node(2)), Node(1, Node(10), Node(5)))
    return Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))


def test_level_order_traverse():
    assert not level_order_traverse(None)

    root = Node(12)
    assert level_order_traverse(root) == [[12]]

    root = get_mock_tree(1)
    assert level_order_traverse(root) == [[12], [7, 1], [9, 10, 5]]

    root = get_mock_tree()
    assert level_order_traverse(root) == [[1], [2, 3], [4, 5, 6, 7]]


def test_reverse_level_order_traverse():
    assert not reverse_level_order_traverse(None)

    root = get_mock_tree(1)
    assert reverse_level_order_traverse(root) == [[9, 10, 5], [7, 1], [12]]

    root = get_mock_tree()
    assert reverse_level_order_traverse(root) == [[4, 5, 6, 7], [2, 3], [1]]


def test_zigzag_level_order_traverse():
    assert not zigzag_level_order_traverse(None)

    root = get_mock_tree(1)
    assert zigzag_level_order_traverse(root) == [[12], [1, 7], [9, 10, 5]]

    root = get_mock_tree()
    assert zigzag_level_order_traverse(root) == [[1], [3, 2], [4, 5, 6, 7]]


def test_find_level_averages():
    assert not find_level_averages(None)

    root = get_mock_tree(4)
    assert find_level_averages(root) == [12, 4, 6.5]

    root = get_mock_tree()
    assert find_level_averages(root) == [1, 2.5, 5.5]


def test_find_minimum_depth():
    assert not find_minimum_depth(None)

    root = get_mock_tree(3)
    assert find_minimum_depth(root) == 2

    root = get_mock_tree()
    assert find_minimum_depth(root) == 3


def test_find_successor():
    assert not find_successor(None, 1)

    root = get_mock_tree(2)
    result = find_successor(root, 3)
    assert result
    assert result.value == 4

    root = get_mock_tree(1)
    result = find_successor(root, 9)
    assert result
    assert result.value == 10


def test_connect_level_order_siblings():
    assert not connect_level_order_siblings(None)

    root = get_mock_tree(1)
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

    root = get_mock_tree(1)
    root = connect_all_siblings(root)
    assert root and root.next and root.next.value == 7
    assert root.next.next and root.next.next.value == 1
    assert root.next.next.next and root.next.next.next.value == 9
    assert root.next.next.next.next and root.next.next.next.next.value == 10
    assert root.next.next.next.next.next
    assert root.next.next.next.next.next.value == 5
    assert not root.next.next.next.next.next.next
