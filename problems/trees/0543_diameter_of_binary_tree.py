"""
543. Diameter of Binary Tree
Topic: Senior, Tree, Depth-First Search, Binary Tree
Difficulty: Easy
Status: Solved
Date: 2026-06-03

Key idea:
- Track depths, store lenght of the longest path seen.
"""

from typing import Optional, Iterable
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# For testing
class Tree:
    def __init__(self, values: Iterable):
        self.root = None

        val_iter = iter(values)
        root_val = next(val_iter, None)
        if root_val is None:
            return

        self.root = TreeNode(root_val)
        queue = deque([self.root])
        while True:
            parent = queue.popleft()
            try:
                left_val = next(val_iter)
                if left_val is not None:
                    left_child = TreeNode(left_val)
                    queue.append(left_child)
                    parent.left = left_child
                else:
                    queue.append(None)
                right_val = next(val_iter)
                if right_val is not None:
                    right_child = TreeNode(right_val)
                    queue.append(right_child)
                    parent.right = right_child
                else:
                    queue.append(None)
            except StopIteration:
                break


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def traverse(subtree_root):
            if subtree_root is None:
                return 0
            left_depth = traverse(subtree_root.left)
            right_depth = traverse(subtree_root.right)

            new_path_length = left_depth + right_depth
            if new_path_length > self.diameter:
                self.diameter = new_path_length

            depth = max(left_depth, right_depth) + 1
            return depth

        traverse(root)
        return self.diameter


def test():
    sol = Solution()

    cases = [
        (
            {
                "root": Tree([1, 2, 3, 4, 5]).root,
            },
            3,
        ),
        (
            {
                "root": Tree([1, 2]).root,
            },
            1,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.diameterOfBinaryTree(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
