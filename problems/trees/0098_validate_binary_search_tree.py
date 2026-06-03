"""
98. Validate Binary Search Tree
Topic: Senior Staff, Tree, Depth-First Search, String Matching, Binary Tree,
  Hash Function
Difficulty: Medium
Status: Solved
Date: 2026-06-03

Key idea:
- Check subtrees passing down allowed values window.
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_subtree(root, float("-inf"), float("inf"))

    def check_subtree(self, root: Optional[TreeNode], low, high):
        if root is None:
            return True

        if not (low < root.val < high):
            return False

        return (
            self.check_subtree(root.left, low, root.val)
            and self.check_subtree(root.right, root.val, high)
        )


def test():
    sol = Solution()

    cases = [
        (
            {
                "root": Tree([2, 1, 3]).root,
            },
            True,
        ),
        (
            {
                "root": Tree([5, 1, 4, None, None, 3, 6]).root,
            },
            False,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.isValidBST(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
