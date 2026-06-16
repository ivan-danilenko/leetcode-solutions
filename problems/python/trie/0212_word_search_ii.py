"""
212. Word Search II
Topic: Array, String, Backtracking, Trie, Matrix
Difficulty: Hard
Status: Solved
Date: 2026-05-20

Key idea:
- Depth First Search
- Keep track of visited cells
- Use trie for tracking of matching prefixes

Possible improvements:
- Mark board in-place instead of using a set.

Mistakes:
- Bug with removal in trie
"""

from typing import List
from collections import Counter


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

    def remove(self, word: str):
        node = self.root
        place_to_delete = None
        for ch in word:
            if (
                place_to_delete is None
                or len(node.children) > 1
                or node.word is not None
            ):
                place_to_delete = node, ch
            node = node.children[ch]

        node.word = None
        if not node.children:
            if place_to_delete is None:
                self.root = TrieNode()
            else:
                node, ch = place_to_delete
                del node.children[ch]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        letter_counter = Counter(ch for word in words for ch in word)
        word_trie = Trie()
        for word in words:
            counter = Counter(ch for ch in word)
            if any(letter_counter[ch] < n for ch, n in counter.items()):
                continue
            word_trie.insert(word)

        height = len(board)
        width = len(board[0])
        displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r, c, trie_node):
            if board[r][c] not in trie_node.children:
                return None

            next_trie_node = trie_node.children[board[r][c]]
            result = set()
            if next_trie_node.word is not None:
                result.add(next_trie_node.word)

            visited.add((r, c))
            for dr, dc in displacements:
                if r + dr < 0 or r + dr == height:
                    continue
                if c + dc < 0 or c + dc == width:
                    continue
                if (r + dr, c + dc) in visited:
                    continue

                words = dfs(r + dr, c + dc, next_trie_node)
                if words is not None:
                    result.update(words)
            visited.remove((r, c))

            return result if result else None

        result = set()
        for r in range(height):
            for c in range(width):
                visited.clear()
                words = dfs(r, c, word_trie.root)
                if words is not None:
                    for w in words:
                        word_trie.remove(w)
                    result.update(words)

        return sorted(result)


def test():
    sol = Solution()

    cases = [
        (
            {
                "board": [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                "words": ["oath", "pea", "eat", "rain"],
            },
            ["eat", "oath"],
        ),
        (
            {
                "board": [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                "words": ["o", "oa", "oat", "oath", "oathv"],
            },
            ["o", "oa", "oat", "oath"],
        ),
        (
            {
                "board": [
                    ["a", "b"],
                    ["c", "d"],
                ],
                "words": ["abcb"],
            },
            [],
        ),
        (
            {
                "board": [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                "words": [
                    "oath",
                    "pea",
                    "eat",
                    "rain",
                    "oathi",
                    "oathk",
                    "oathf",
                    "oate",
                    "oathii",
                    "oathfi",
                    "oathfii",
                ],
            },
            [
                "eat",
                "oate",
                "oath",
                "oathf",
                "oathfi",
                "oathfii",
                "oathi",
                "oathii",
                "oathk",
            ],
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        print(f"running test {i}")
        got = sol.findWords(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
