"""
572. Subtree of Another Tree
Topic: Senior Staff, Tree, Depth-First Search, String Matching, Binary Tree,
  Hash Function
Difficulty: Easy
Status: Solved
Date: 2026-06-03

Key idea:
- Dfs and using Leetcode 100 [Same Tree]

Possible improvements:
- If trees are expected to have many repeated values
  [e.g. all values are the same] then we can add
  a cheap filter to terminate early, e.g. size or
  depth of subtree.
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None

        return (
            self.is_same_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def is_same_tree(self, p, q):
        if p is None or q is None:
            return p is q
        return (
            p.val == q.val
            and self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right)
        )


def test():
    sol = Solution()

    cases = [
        (
            {
                "root": Tree([3, 4, 5, 1, 2]).root,
                "subRoot": Tree([4, 1, 2]).root,
            },
            True,
        ),
        (
            {
                "root": Tree([3, 4, 5, 1, 2, None, None, None, None, 0]).root,
                "subRoot": Tree([4, 1, 2]).root,
            },
            False,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.isSubtree(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
