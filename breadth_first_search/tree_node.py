"""
Node of a binary tree
"""


class TreeNode:

    def __init__(self, value: int, left: 'TreeNode' = None, right: 'TreeNode' = None, next: 'TreeNode' = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

    # level order traversal using 'next' pointer
    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.val) + " ", end='')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()
