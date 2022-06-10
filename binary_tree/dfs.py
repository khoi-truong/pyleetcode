"""
This pattern is based on the Depth First Search (DFS) technique to traverse a \
tree.

We will be using recursion (or we can also use a stack for the iterative \
approach) to keep track of all the previous (parent) nodes while traversing. \
This also means that the space complexity of the algorithm will be O(H), where \
`H` is the maximum height of the tree.
"""

from typing import List, Optional

from binary_tree.tree_node import TreeNode


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
    return has_path(root.left, target_sum - root.value) or \
        has_path(root.right, target_sum - root.value)


def find_paths(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Problem:
        https://leetcode.com/problems/path-sum-ii/

    Given a binary tree and a target sum, find all root-to-leaf paths where \
    each path's sum equals the given target sum.
    """
    if not root:
        return []
    all_paths = []
    _find_paths(root, target_sum, [], all_paths)
    return all_paths


def _find_paths(
        node: Optional[TreeNode],
        required_sum: int,
        path: List[int],
        all_paths: List[List[int]]):
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
