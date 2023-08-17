"""
This pattern is based on the Depth First Search (DFS) technique to traverse a \
tree.

We will be using recursion (or we can also use a stack for the iterative \
approach) to keep track of all the previous (parent) nodes while traversing. \
This also means that the space complexity of the algorithm will be O(H), where \
`H` is the maximum height of the tree.
"""
from typing import Optional

from .tree_node import TreeNode


def has_path(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    Problem:
        https://leetcode.com/problems/path-sum/

    Given a binary tree and a target sum, determine if the tree has a \
    root-to-leaf path such that adding up all the values along the path equals \
    the given target sum.
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.value == target_sum
    return has_path(root.left, target_sum - root.value) or has_path(
        root.right, target_sum - root.value
    )


def find_paths(root: Optional[TreeNode], target_sum: int) -> list[list[int]]:
    """
    Problem:
        https://leetcode.com/problems/path-sum-ii/

    Given a binary tree and a target sum, find all root-to-leaf paths where \
    each path's sum equals the given target sum.
    """
    if not root:
        return []
    all_paths = list[list[int]]()
    _find_paths(root, target_sum, [], all_paths)
    return all_paths


def _find_paths(
    node: Optional[TreeNode],
    required_sum: int,
    path: list[int],
    all_paths: list[list[int]],
):
    if not node:
        return
    path.append(node.value)
    if not node.left and not node.right and node.value == required_sum:
        all_paths.append(list(path))
    _find_paths(node.left, required_sum - node.value, path, all_paths)
    _find_paths(node.right, required_sum - node.value, path, all_paths)
    path.pop()


def find_sum_of_path_numbers(root: Optional[TreeNode]) -> int:
    """
    Problem:
        https://leetcode.com/problems/sum-root-to-leaf-numbers/

    Given a binary tree, find the sum of all root-to-leaf numbers.
    """
    return _find_sum_of_path_numbers(root, 0)


def _find_sum_of_path_numbers(node: Optional[TreeNode], path_sum: int) -> int:
    if not node:
        return 0
    path_sum = path_sum * 10 + node.value
    if not node.left and not node.right:
        return path_sum
    left_sum = _find_sum_of_path_numbers(node.left, path_sum)
    right_sum = _find_sum_of_path_numbers(node.right, path_sum)
    return left_sum + right_sum


def find_path(root: Optional[TreeNode], sequence: list[int]) -> bool:
    """
    Problem:
        https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

    Given a binary tree where each path going from the root to any leaf form a \
    valid sequence, check if a given string is a valid sequence in such binary \
    tree.
    """
    if not root:
        return len(sequence) == 0
    return _find_path(root, sequence, 0)


def _find_path(node: Optional[TreeNode], sequence: list[int], index: int) -> bool:
    if not node:
        return False
    length = len(sequence)
    if index >= length or node.value != sequence[index]:
        return False
    if not node.left and not node.right and index == length - 1:
        return True
    find_path_in_left = _find_path(node.left, sequence, index + 1)
    find_path_in_right = _find_path(node.right, sequence, index + 1)
    return find_path_in_left or find_path_in_right


def count_paths(root: Optional[TreeNode], target_sum: int) -> int:
    """
    Problems:
        https://leetcode.com/problems/path-sum-iii/

    Given the root of a binary tree and an integer targetSum, return the \
    number of paths where the sum of the values along the path equals targetSum.

    The path does not need to start or end at the root or a leaf, but it must \
    go downwards (i.e., traveling only from parent nodes to child nodes).
    """
    return _count_paths(root, target_sum, [])


def _count_paths(node: Optional[TreeNode], target_sum: int, path: list[int]) -> int:
    if not node:
        return 0

    path.append(node.value)
    path_count = 0
    path_sum = 0
    for i in range(len(path) - 1, -1, -1):
        path_sum += path[i]
        if path_sum == target_sum:
            path_count += 1

    path_count += _count_paths(node.left, target_sum, path)
    path_count += _count_paths(node.right, target_sum, path)

    path.pop()

    return path_count
