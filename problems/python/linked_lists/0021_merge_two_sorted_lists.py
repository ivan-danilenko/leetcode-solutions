"""
21. Merge Two Sorted Lists
Topic: Linked List, Recursion
Difficulty: Easy
Status: Solved
Date: 2026-05-19

Key idea:
-

Mistakes:
- Attaching remaining list can be done faster
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        zero_node = ListNode(None, None)
        curr_node = zero_node

        while curr1 is not None and curr2 is not None:
            prev_node = curr_node

            if curr1.val <= curr2.val:
                val = curr1.val
                curr1 = curr1.next
            else:
                val = curr2.val
                curr2 = curr2.next

            curr_node = ListNode(val, None)
            prev_node.next = curr_node

        # attach remaining nodes
        if curr1 is None:
            curr_node.next = curr2
        else:
            curr_node.next = curr1

        return zero_node.next


def test():
    sol = Solution()

    class LinkedList:
        def __init__(self, iterable=None, first_node=None):
            assert (
                iterable is None or first_node is None
            ), "Incorrect initialization data"

            if iterable is None:
                self.first_node = first_node
                return

            iter_ = iter(iterable)
            try:
                self.first_node = ListNode(val=next(iter_), next=None)
                prev_node = self.first_node
            except StopIteration:
                self.first_node = None
                return

            for val in iter_:
                new_node = ListNode(val=val, next=None)
                prev_node.next = new_node
                prev_node = new_node

        def __iter__(self):
            curr_node = self.first_node
            while curr_node is not None:
                yield curr_node.val
                curr_node = curr_node.next

        def __eq__(self, other):
            try:
                return all(x == y for x, y in zip(self, other, strict=True))
            except ValueError:
                return False

        def __str__(self):
            return " ".join(str(val) for val in self)

    cases = [
        (
            {
                "list1": LinkedList(iterable=[1, 2, 4]).first_node,
                "list2": LinkedList(iterable=[1, 3, 4]).first_node,
            },
            LinkedList(iterable=[1, 1, 2, 3, 4, 4]),
        ),
        (
            {
                "list1": LinkedList(iterable=[]).first_node,
                "list2": LinkedList(iterable=[]).first_node,
            },
            LinkedList([]),
        ),
        (
            {
                "list1": LinkedList(iterable=[]).first_node,
                "list2": LinkedList(iterable=[0]).first_node,
            },
            LinkedList([0]),
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = LinkedList(first_node=sol.mergeTwoLists(**kwargs))
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
