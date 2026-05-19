"""
23. Merge Two Sorted Lists
Topic: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
Difficulty: Hard
Status: Solved
Date: 2026-05-19

Key idea:
- Use heap to generalize to `k` lists from the case of 2 lists.

Mistakes:
- Forgot to heapify first
"""

from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def key(node1, node2):
            return node1.val <= node2.val

        # list_index is added to avoid comparison between ListNodes
        # if we had more control over `ListNode`: define `__leq__` there
        # to avoid storing triples and better readability
        heap = [
            (node.val, list_index, node)
            for list_index, node in enumerate(lists)
            if node is not None
        ]

        if not heap:
            return None

        heapq.heapify(heap)

        zero_node = ListNode(None, None)
        curr_node = zero_node

        while len(heap) > 1:
            prev_node = curr_node

            val, list_index, node = heapq.heappop(heap)

            if node.next is not None:
                new_node = node.next
                heapq.heappush(heap, (new_node.val, list_index, new_node))

            curr_node = ListNode(val, None)
            prev_node.next = curr_node

        # attach remaining nodes
        curr_node.next = heap[0][2]

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
                "lists": [
                    LinkedList(iterable=[1, 4, 5]).first_node,
                    LinkedList(iterable=[1, 3, 4]).first_node,
                    LinkedList(iterable=[2, 6]).first_node,
                ]
            },
            LinkedList(iterable=[1, 1, 2, 3, 4, 4, 5, 6]),
        ),
        (
            {"lists": []},
            LinkedList(iterable=[]),
        ),
        (
            {
                "lists": [
                    LinkedList(iterable=[1]).first_node,
                    LinkedList(iterable=[0]).first_node,
                ]
            },
            LinkedList(iterable=[0, 1]),
        ),
        (
            {
                "lists": [
                    LinkedList(iterable=[]).first_node,
                ]
            },
            LinkedList(iterable=[]),
        ),
        (
            {
                "lists": [
                    LinkedList(iterable=[1, 2, 4]).first_node,
                    LinkedList(iterable=[1, 3, 4]).first_node,
                ]
            },
            LinkedList(iterable=[1, 1, 2, 3, 4, 4]),
        ),
        (
            {
                "lists": [
                    LinkedList(iterable=[]).first_node,
                    LinkedList(iterable=[]).first_node,
                ]
            },
            LinkedList([]),
        ),
        (
            {
                "lists": [
                    LinkedList(iterable=[]).first_node,
                    LinkedList(iterable=[0]).first_node,
                ]
            },
            LinkedList([0]),
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = LinkedList(first_node=sol.mergeKLists(**kwargs))
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
