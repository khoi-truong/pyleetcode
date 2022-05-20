"""
BFS traversal problems
"""
from collections import deque

from .tree_node import TreeNode


def level_order_traverse(root: TreeNode):
    """
    Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

    Given a binary tree, populate an array to represent its level-by-level \
    traversal. You should populate the values of all nodes of each level from \
    left to right in separate sub-arrays.
    """
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


def reverse_level_order_traverse(root: TreeNode):
    """
    Problem: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

    Given a binary tree, populate an array to represent its level-by-level \
    traversal in reverse order, i.e., the lowest level comes first. You should \
    populate the values of all nodes in each level from left to right in \
    separate sub-arrays.
    """
    if root is None:
        return []

    result = deque()
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
        result.appendleft(current_level)
    return list(result)

def zigzag_level_order_traverse(root: TreeNode):
    """
    Problem: \
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

    Given a binary tree, populate an array to represent its zigzag level order \
    traversal. You should populate the values of all nodes of the first level \
    from left to right, then right to left for the next level and keep \
    alternating in the same manner for the following levels.
    """
    result = []
    queue = deque()
    queue.append(root)
    level = 0
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            current_node: TreeNode = queue.popleft()
            if level % 2 == 0:
                current_level.append(current_node.value)
            else:
                current_level.appendleft(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        level += 1
        result.append(list(current_level))
    return result
