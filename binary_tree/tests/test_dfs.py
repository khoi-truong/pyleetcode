"""
Unit tests for DFS problems
"""
from binary_tree.dfs import (count_paths, find_path, find_paths,
                             find_sum_of_path_numbers, has_path)

from ..tree_node import TreeNode as Node


def get_mock_tree(number: int = 0) -> Node:
    if number == 1:
        return Node(1,
                    Node(7,
                         Node(4),
                         Node(5)),
                    Node(9,
                         Node(2),
                         Node(7)))
    elif number == 2:
        return Node(12,
                    Node(7,
                         Node(9)),
                    Node(1,
                         Node(10),
                         Node(5)))
    elif number == 3:
        return Node(12,
                    Node(7,
                         Node(4)),
                    Node(1,
                         Node(10),
                         Node(5)))
    elif number == 4:
        return Node(1,
                    Node(7),
                    Node(9,
                         Node(2),
                         Node(9)))
    elif number == 5:
        return Node(1,
                    Node(0,
                         Node(1)),
                    Node(1,
                         Node(6),
                         Node(5)))
    elif number == 6:
        return Node(1,
                    Node(7,
                         Node(6),
                         Node(5)),
                    Node(9,
                         Node(2),
                         Node(3)))
    return Node(1,
                Node(2,
                     Node(4),
                     Node(5)),
                Node(3,
                     Node(6),
                     Node(7)))


def test_has_path_with_sum():
    assert not has_path(None, 10)

    root = get_mock_tree()
    assert has_path(root, 10)

    root = get_mock_tree(2)
    assert has_path(root, 23)
    assert not has_path(root, 16)


def test_find_paths_with_sum():
    assert not find_paths(None, 10)

    root = get_mock_tree(1)
    assert find_paths(root, 12) == [[1, 7, 4], [1, 9, 2]]

    root = get_mock_tree(3)
    assert find_paths(root, 23) == [[12, 7, 4], [12, 1, 10]]


def test_find_sum_of_path_numbers():
    assert not find_sum_of_path_numbers(None)

    root = get_mock_tree(4)
    assert find_sum_of_path_numbers(root) == 408

    root = get_mock_tree(5)
    assert find_sum_of_path_numbers(root) == 332


def test_find_path():
    assert find_path(None, [])
    assert find_path(Node(1), [1])
    assert find_path(get_mock_tree(), [1, 3, 6])
    assert find_path(get_mock_tree(4), [1, 9, 9])


def test_count_paths():
    assert count_paths(None, 10) == 0
    assert count_paths(Node(1), 10) == 0
    assert count_paths(Node(10), 10) == 1
    assert count_paths(get_mock_tree(3), 11) == 2
    assert count_paths(get_mock_tree(6), 12) == 3
