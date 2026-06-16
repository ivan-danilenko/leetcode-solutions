"""
637. Average of Levels in Binary Tree
Topic: Senior Staff, Tree, Depth-First Search, String Matching, Binary Tree,
  Hash Function
Difficulty: Easy
Status: Solved
Date: 2026-06-03

Key idea:
- Use dict counters per level
"""

from typing import Optional, Iterable, List
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes_on_level = []
        value_sum_on_level = []

        def dfs(subtree_root, level):
            if subtree_root is None:
                return
            if level == len(nodes_on_level):
                nodes_on_level.append(0)
                value_sum_on_level.append(0)
            nodes_on_level[level] += 1
            value_sum_on_level[level] += subtree_root.val
            dfs(subtree_root.left, level + 1)
            dfs(subtree_root.right, level + 1)

        dfs(root, 0)
        result = [
            value_sum_on_level[i] / nodes_on_level[i]
            for i in range(len(nodes_on_level))
        ]

        return result


def test():
    sol = Solution()

    cases = [
        (
            {
                "root": Tree([3, 9, 20, None, None, 15, 7]).root,
            },
            [3.00000, 14.50000, 11.00000],
        ),
        (
            {
                "root": Tree([3, 9, 20, 15, 7]).root,
            },
            [3.00000, 14.50000, 11.00000],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.averageOfLevels(**kwargs)
        tol = 0.00001
        assert all(
            abs(g - e) < tol for g, e in zip(got, expected, strict=True)
        ), f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
