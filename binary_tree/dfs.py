"""
This pattern is based on the Depth First Search (DFS) technique to traverse a \
tree.

We will be using recursion (or we can also use a stack for the iterative \
approach) to keep track of all the previous (parent) nodes while traversing. \
This also means that the space complexity of the algorithm will be O(H), where \
`H` is the maximum height of the tree.
"""

from typing import Optional

from binary_tree.tree_node import TreeNode


def has_path(root: Optional[TreeNode], summary: int) -> bool:
    """
    Given a binary tree and a summary, determine if the tree has a \
    root-to-leaf path such that adding up all the values along the path equals \
    the given summary.
    """
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.value == summary
    return has_path(root.left, summary - root.value) or \
        has_path(root.right, summary - root.value)
