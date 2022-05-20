"""
Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, populate an array to represent its level-by-level \
    traversal. You should populate the values of all nodes of each level \
    from left to right in separate sub-arrays.
"""
from collections import deque

from .tree_node import TreeNode


def traverse(root: TreeNode):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node: TreeNode = queue.popleft()
            current_level.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
    return result
