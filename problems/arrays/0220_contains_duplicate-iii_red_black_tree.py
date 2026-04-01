"""
220. Contains Duplicate III
Topic: Array, Sliding Window, Sorting, Bucket Sort, Ordered Set
Difficulty: Hard
Status: Solved
Date: 2026-03-23

Key idea:
- Sliding window keeps track of last
- Use Red Black Tree for the window.

Mistakes:
- Implementation of Red Black Trees had issues
"""

from typing import List, Iterable, Optional
from dataclasses import dataclass
from itertools import islice


@dataclass(slots=True)
class RedBlueTreeNode:
    value: int
    parent: Optional["RedBlueTreeNode"] = None
    # `color` is `True` if black, `False` if red
    color: bool = False
    left: Optional["RedBlueTreeNode"] = None
    right: Optional["RedBlueTreeNode"] | None = None

    def is_black(self):
        return self.color

    def is_red(self):
        return not self.color

    def set_black(self):
        self.color = True

    def set_red(self):
        self.color = False

    def is_root(self):
        return self.parent is None

    def is_left_child(self):
        return self.parent.left is self

    def is_right_child(self):
        return self.parent.right is self

    def __repr__(self):
        parent_value = None if self.parent is None else self.parent.value
        left_value = None if self.left is None else self.left.value
        right_value = None if self.right is None else self.right.value
        result = f"RedBlueTreeNode(value={self.value}, "
        result += f"parent={parent_value}, "
        result += f"color={self.color}, "
        result += f"left={left_value} "
        result += f"right={right_value})"
        return result


class RedBlackTree:
    class ReachedEndError(RuntimeError):
        pass

    def __init__(self, iterable: Iterable):
        self.root = None
        self.length = 0
        for value in iterable:
            self.insert(value)

    def __len__(self):
        return self.length

    def __iter__(self):
        if len(self) == 0:
            return
        node = self.min_node()
        yield node
        for _ in range(len(self) - 1):
            node = self.next_node(node)
            yield node

    def delete(self, value):
        current_node = self.find(value)

        if current_node is not None:
            self._delete_node(current_node)
            self.length -= 1

    def find(self, value):
        current_node = self.root
        while current_node is not None and current_node.value != value:
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return current_node

    def min_node(self):
        if self.root is None:
            return None
        return self._min_node_in_branch(self.root)

    def max_node(self):
        if self.root is None:
            return None
        return self._max_node_in_branch(self.root)

    def _min_node_in_branch(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _max_node_in_branch(self, node):
        while node.right is not None:
            node = node.right
        return node

    def next_node(self, node):
        if node.right is not None:
            return self._min_node_in_branch(node.right)
        while node.parent is not None:
            if node.is_left_child():
                return node.parent
            node = node.parent

        # reached the root, so the original was the max element
        raise self.ReachedEndError("The element is maximal, no next")

    def prev_node(self, node):
        if node.left is not None:
            return self._max_node_in_branch(node.left)
        while node.parent is not None:
            if node.is_right_child():
                return node.parent
            node = node.parent

        # reached the root, so the original was the min element
        raise self.ReachedEndError("The element is minimal, no next")

    def _replace_node(self, old_node, new_node):
        if old_node.parent is None:
            self.root = new_node
        elif old_node.is_left_child():
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node

        if new_node is not None:
            new_node.parent = old_node.parent

    def _delete_node(self, node):
        removed_node = node
        removed_was_black = removed_node.is_black()

        if node.left is None:
            fix_node = node.right
            fix_parent = node.parent
            self._replace_node(node, node.right)

        elif node.right is None:
            fix_node = node.left
            fix_parent = node.parent
            self._replace_node(node, node.left)

        else:
            removed_node = self._min_node_in_branch(node.right)
            removed_was_black = removed_node.is_black()
            fix_node = removed_node.right

            if removed_node.parent is node:
                fix_parent = removed_node
            else:
                fix_parent = removed_node.parent
                self._replace_node(removed_node, removed_node.right)
                removed_node.right = node.right
                removed_node.right.parent = removed_node

            self._replace_node(node, removed_node)
            removed_node.left = node.left
            removed_node.left.parent = removed_node
            removed_node.color = node.color

        if removed_was_black:
            self._fix_double_blacks(fix_node, fix_parent)

        if self.root is not None:
            self.root.set_black()

    def _fix_double_blacks(self, node, parent):
        while node is not self.root and (node is None or node.is_black()):
            if parent is None:
                break

            if node is parent.left:
                sibling = parent.right

                if sibling is not None and sibling.is_red():
                    sibling.set_black()
                    parent.set_red()
                    self._left_rotate(parent)
                    sibling = parent.right

                sibling_left = None if sibling is None else sibling.left
                sibling_right = None if sibling is None else sibling.right

                if (sibling_left is None or sibling_left.is_black()) and (
                    sibling_right is None or sibling_right.is_black()
                ):
                    if sibling is not None:
                        sibling.set_red()
                    node = parent
                    parent = node.parent
                else:
                    if sibling_right is None or sibling_right.is_black():
                        if sibling_left is not None:
                            sibling_left.set_black()
                        if sibling is not None:
                            sibling.set_red()
                            self._right_rotate(sibling)
                        sibling = parent.right

                    if sibling is not None:
                        sibling.color = parent.color
                    parent.set_black()
                    if sibling is not None and sibling.right is not None:
                        sibling.right.set_black()
                    self._left_rotate(parent)
                    node = self.root
                    parent = None

            else:
                sibling = parent.left

                if sibling is not None and sibling.is_red():
                    sibling.set_black()
                    parent.set_red()
                    self._right_rotate(parent)
                    sibling = parent.left

                sibling_left = None if sibling is None else sibling.left
                sibling_right = None if sibling is None else sibling.right

                if (sibling_left is None or sibling_left.is_black()) and (
                    sibling_right is None or sibling_right.is_black()
                ):
                    if sibling is not None:
                        sibling.set_red()
                    node = parent
                    parent = node.parent
                else:
                    if sibling_left is None or sibling_left.is_black():
                        if sibling_right is not None:
                            sibling_right.set_black()
                        if sibling is not None:
                            sibling.set_red()
                            self._left_rotate(sibling)
                        sibling = parent.left

                    if sibling is not None:
                        sibling.color = parent.color
                    parent.set_black()
                    if sibling is not None and sibling.left is not None:
                        sibling.left.set_black()
                    self._right_rotate(parent)
                    node = self.root
                    parent = None

        if node is not None:
            node.set_black()

    def insert(self, value):
        self.length += 1
        new_node = RedBlueTreeNode(value)
        if self.root is None:
            self.root = new_node
            self.root.set_black()
            return

        current_node = self.root
        parent_node = None
        while current_node is not None:
            parent_node = current_node
            if new_node.value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = parent_node

        if new_node.value < parent_node.value:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

        self._fix_double_reds(new_node)

    def _sibling(self, node):
        if node.parent is None:
            return None
        if node.is_left_child():
            return node.parent.right
        else:
            return node.parent.left

    def _uncle(self, node):
        if node.parent is None:
            return None

        return self._sibling(node.parent)

    def _fix_double_reds(self, node):
        if node.is_root():
            node.set_black()
            return

        parent = node.parent
        if parent.is_red():
            grandparent = parent.parent
            uncle = self._uncle(node)
            if uncle is not None and uncle.is_red():
                parent.set_black()
                uncle.set_black()
                grandparent.set_red()
                self._fix_double_reds(grandparent)
            elif parent.is_left_child():
                if node.is_left_child():
                    parent.color, grandparent.color = grandparent.color, parent.color
                else:
                    self._left_rotate(parent)
                    node.color, grandparent.color = grandparent.color, node.color
                self._right_rotate(grandparent)
            else:
                if node.is_right_child():
                    parent.color, grandparent.color = grandparent.color, parent.color
                else:
                    self._right_rotate(parent)
                    node.color, grandparent.color = grandparent.color, node.color
                self._left_rotate(grandparent)

    def _left_rotate(self, node):
        new_parent = node.right

        node.right = new_parent.left
        if new_parent.left is not None:
            new_parent.left.parent = node

        new_parent.parent = node.parent
        if node.is_root():
            self.root = new_parent
        elif node.is_left_child():
            node.parent.left = new_parent
        else:
            node.parent.right = new_parent

        new_parent.left = node
        node.parent = new_parent

    def _right_rotate(self, node):
        new_parent = node.left

        node.left = new_parent.right
        if new_parent.right is not None:
            new_parent.right.parent = node

        new_parent.parent = node.parent
        if node.is_root():
            self.root = new_parent
        elif node.is_right_child():
            node.parent.right = new_parent
        else:
            node.parent.left = new_parent

        new_parent.right = node
        node.parent = new_parent

    def replace(self, old_value, new_value):
        if old_value == new_value:
            return
        self.delete(old_value)
        self.insert(new_value)

    def print_in_order(self):
        print("In order:")
        if self.root is None:
            print("Empty")
        else:
            print(self._repr_inorder(self.root))
        print()

    def _repr_inorder(self, x):
        if x is None:
            return
        result = repr(x.value)
        left_piece = self._repr_inorder(x.left)
        if left_piece is not None:
            result = left_piece + " " + result
        right_piece = self._repr_inorder(x.right)
        if right_piece is not None:
            result = result + " " + right_piece
        return result


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        window = RedBlackTree(islice(nums, indexDiff + 1))

        window_iter = iter(window)
        # skip the first element
        prev_node = next(window_iter)
        for next_node in window_iter:
            if next_node.value - prev_node.value <= valueDiff:
                return True
            prev_node = next_node

        for i in range(len(nums) - indexDiff - 1):
            old_value = nums[i]
            new_value = nums[i + indexDiff + 1]
            if new_value != old_value:
                window.delete(old_value)
                window.insert(new_value)

            inserted_node = window.find(new_value)

            try:
                next_node = window.next_node(inserted_node)
                if next_node.value - inserted_node.value <= valueDiff:
                    return True
            except RedBlackTree.ReachedEndError:
                pass
            try:
                prev_node = window.prev_node(inserted_node)
                if inserted_node.value - prev_node.value <= valueDiff:
                    return True
            except RedBlackTree.ReachedEndError:
                pass

        return False


def test():
    sol = Solution()

    cases = [
        (
            {
                "nums": [1, 2, 3, 1],
                "indexDiff": 3,
                "valueDiff": 0,
            },
            True,
        ),
        (
            {
                "nums": [1, 5, 9, 1, 5, 9],
                "indexDiff": 2,
                "valueDiff": 3,
            },
            False,
        ),
        (
            {
                "nums": [1, 5, 9, 0, 4, 8],
                "indexDiff": 2,
                "valueDiff": 3,
            },
            False,
        ),
        (
            {
                "nums": [0, 1, 2, 3, 0, 2],
                "indexDiff": 3,
                "valueDiff": 0,
            },
            True,
        ),
        (
            {
                "nums": [-3, 3],
                "indexDiff": 2,
                "valueDiff": 4,
            },
            False,
        ),
        (
            {
                "nums": [-2, 3],
                "indexDiff": 2,
                "valueDiff": 5,
            },
            True,
        ),
        (
            {
                "nums": [1, 2, 1, 1],
                "indexDiff": 1,
                "valueDiff": 0,
            },
            True,
        ),
        (
            {
                "nums": [1, 2, 5, 6, 7, 2, 4],
                "indexDiff": 4,
                "valueDiff": 0,
            },
            True,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.containsNearbyAlmostDuplicate(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
