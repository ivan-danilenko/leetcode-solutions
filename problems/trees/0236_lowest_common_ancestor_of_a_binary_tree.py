"""
236. Lowest Common Ancestor of a Binary Tree
Topic: Tree, Depth-First Search, Binary Tree
Difficulty: Medium
Status: Solved
Date: 2026-06-08

Key idea:
- Similar to Leetcode 543, just keep track of different data.
"""

from typing import Iterable
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
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        if p.val == root.val or q.val == root.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        return left if left is not None else right


def test():
    sol = Solution()

    cases = [
        (
            {
                "root": Tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]).root,
                "p": TreeNode(5),
                "q": TreeNode(1),
            },
            TreeNode(3),
        ),
        (
            {
                "root": Tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]).root,
                "p": TreeNode(5),
                "q": TreeNode(4),
            },
            TreeNode(5),
        ),
        (
            {
                "root": Tree([1, 2]).root,
                "p": TreeNode(1),
                "q": TreeNode(2),
            },
            TreeNode(1),
        ),
        (
            {
                "root": Tree([1, 2, 3, None, 4]).root,
                "p": TreeNode(4),
                "q": TreeNode(3),
            },
            TreeNode(1),
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.lowestCommonAncestor(**kwargs)
        assert (
            got.val == expected.val
        ), f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
