"""
BFS traversal problems
"""
from collections import deque
from typing import Optional

from .tree_node import TreeNode


def level_order_traverse(root: Optional[TreeNode]) -> list[list[int]]:
    """
    Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

    Given a binary tree, populate an array to represent its level-by-level \
    traversal. You should populate the values of all nodes of each level from \
    left to right in separate sub-arrays.
    """
    result = list[list[int]]()
    if not root:
        return result
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = list[int]()
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
    return result


def reverse_level_order_traverse(root: Optional[TreeNode]) -> list[list[int]]:
    """
    Problem: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

    Given a binary tree, populate an array to represent its level-by-level \
    traversal in reverse order, i.e., the lowest level comes first. You should \
    populate the values of all nodes in each level from left to right in \
    separate sub-arrays.
    """
    if not root:
        return []

    result = deque[list[int]]()
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = list[int]()
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.appendleft(current_level)
    return list(result)


def zigzag_level_order_traverse(root: Optional[TreeNode]) -> list[list[int]]:
    """
    Problem: \
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

    Given a binary tree, populate an array to represent its zigzag level order \
    traversal. You should populate the values of all nodes of the first level \
    from left to right, then right to left for the next level and keep \
    alternating in the same manner for the following levels.
    """
    if not root:
        return []

    result = list[list[int]]()
    queue = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque[int]()
        for _ in range(level_size):
            current_node = queue.popleft()
            if left_to_right:
                current_level.append(current_node.value)
            else:
                current_level.appendleft(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        left_to_right = not left_to_right
        result.append(list(current_level))
    return result


def find_level_averages(root: Optional[TreeNode]) -> list[float]:
    """
    Problem: \
    https://leetcode.com/problems/average-of-levels-in-binary-tree/

    Given a binary tree, populate an array to represent the averages of all of \
    its levels.
    """
    if not root:
        return []
    result = list[float]()
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            current_node = queue.popleft()
            level_sum += current_node.value
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(level_sum / level_size)
    return result


def find_minimum_depth(root: Optional[TreeNode]):
    """
    Problem: \
    https://leetcode.com/problems/minimum-depth-of-binary-tree/

    Find the minimum depth of a binary tree.
    The minimum depth is the number of nodes along the shortest path from the \
    root node to the nearest leaf node.
    """
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            if not current_node.left and not current_node.right:
                return depth
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return depth


def find_successor(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    Given a binary tree and a node, find the level order successor of the \
    given node in the tree.
    The level order successor is the node that appears right after the given \
    node in the level order traversal.
    """
    if not root:
        return None
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        if current_node.value == key:
            break
    return queue[0] if queue else None


def connect_level_order_siblings(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Problem: \
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

    Populate each next pointer to point to its next right node.
    If there is no next right node, the next pointer should be set to NULL.
    """
    if not root:
        return None
    queue = deque([root])
    while queue:
        previous_node: Optional[TreeNode] = None
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            if previous_node:
                previous_node.next = current_node
            previous_node = current_node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return root


def connect_all_siblings(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Given a binary tree, connect each node with its level order successor.
    The last node of each level should point to the first node of the next\
    level.
    """
    if not root:
        return None
    queue = deque([root])
    previous_node: Optional[TreeNode] = None
    while queue:
        current_node = queue.popleft()
        if previous_node:
            previous_node.next = current_node
        previous_node = current_node
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return root


def tree_right_view(root: Optional[TreeNode]) -> list[TreeNode]:
    """
    Problem: \
    https://leetcode.com/problems/binary-tree-right-side-view/

    Given a binary tree, return an array containing nodes in its right view.
    The right view of a binary tree is the set of nodes visible when the tree \
    is seen from the right side.
    """
    if not root:
        return []
    result = list[TreeNode]()
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for index_in_level in range(level_size):
            current_node = queue.popleft()
            if index_in_level == level_size - 1:
                result.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return result
