"""
235. Lowest Common Ancestor of a Binary Search Tree
Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Difficulty: Medium
Status: Solved
Date: 2026-06-08

Key idea:
- Do simultaneous binary search for both numbers.
- Stop when have to choose different branches.
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
        curr_node = root
        left, right = (p, q) if p.val < q.val else (q, p)
        while True:
            if right.val < curr_node.val:
                curr_node = curr_node.left
            elif left.val > curr_node.val:
                curr_node = curr_node.right
            else:
                return curr_node


def test():
    sol = Solution()

    cases = [
        (
            {
                "root": Tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]).root,
                "p": TreeNode(2),
                "q": TreeNode(4),
            },
            TreeNode(2),
        ),
        (
            {
                "root": Tree([2, 1]).root,
                "p": TreeNode(2),
                "q": TreeNode(1),
            },
            TreeNode(2),
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
