"""
827. Making A Large Island
Topic: Principal, Array, Depth-First Search, Breadth-First Search,
  Union-Find, Matrix, Weekly Contest 82
Difficulty: Hard
Status: Solved
Date: 2026-03-20

Key idea:
- Scan row-by-row, remembering what happened at the previous row
- Keep track of coastline ("sea" next to "islands") and islands
- For islands keep track of islands that represent the "name" of the island
- When islands merge islands are identified
- Keep track of island sizes
- For coastline keep track of neighboring islands

Mistakes:
- If no coastline, it could be the case that everything is sea,
  not only one island
- Mistake in indices.
- when deleted a island did not clear value in `island_sizes`
- when merging two islands we need to identify not only these two islands, but
  also all islands previously identified with them
"""

from typing import List
from dataclasses import dataclass
from collections import defaultdict, deque


# a mutable version of `int`
@dataclass(slots=True)
class Island:
    name: int


class Archipelago:
    def __init__(self):
        self.counter = 0
        # `all_names[name]` is all instances of `Island` with this `name`.
        self.all_names = {}
        self.island_sizes = defaultdict(int)

    def newIsland(self):
        new_island = Island(self.counter)
        self.counter += 1
        self.all_names[new_island.name] = [new_island]
        return new_island

    def mergedIsland(self, isl1, isl2):
        if isl1.name == isl2.name:
            return self.all_names[isl1.name][0]

        kept_name = isl1.name
        obsolete_name = isl2.name
        for alias in self.all_names[obsolete_name]:
            alias.name = kept_name
        self.island_sizes[kept_name] += self.island_sizes[obsolete_name]
        del self.island_sizes[obsolete_name]
        self.all_names[kept_name] += self.all_names[obsolete_name]
        del self.all_names[obsolete_name]
        return self.all_names[kept_name][0]

    def islandFromNeighbors(self, left_island, top_island):
        if left_island is None and top_island is None:
            return self.newIsland()
        if left_island is None:
            return top_island
        if top_island is None:
            return left_island
        return self.mergedIsland(left_island, top_island)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        archipelago = Archipelago()
        shared_coastline = deque()
        islands_current_row = {}
        coastline_current_row = {}
        for i in range(len(grid)):
            left_island = None
            islands_row_above = islands_current_row
            islands_current_row = {}
            coastline_row_above = coastline_current_row
            coastline_current_row = defaultdict(list)
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    top_island = islands_row_above.get(j, None)
                    island = archipelago.islandFromNeighbors(left_island, top_island)
                    islands_current_row[j] = island
                    archipelago.island_sizes[island.name] += 1

                    # sea above
                    if i != 0 and top_island is None:
                        coastline_row_above[j].append(island)
                    # see to the left
                    if j != 0 and left_island is None:
                        coastline_current_row[j - 1].append(island)

                    left_island = island

                elif grid[i][j] == 0:
                    if left_island is not None:
                        coastline_current_row[j].append(left_island)
                    # looking for the island above
                    if j in islands_row_above:
                        coastline_current_row[j].append(islands_row_above[j])

                    left_island = None

            # no need to check coastlines to one island,
            # record only coastline shared by at least two islands
            shared_coastline.extend(
                cl for cl in coastline_row_above.values() if len(cl) > 1
            )

        # coastline on the last row has not been added
        shared_coastline.extend(
            cl for cl in coastline_current_row.values() if len(cl) > 1
        )

        # islands do not have shared coastline only if
        # we got not touching islands or everything is sea
        if not shared_coastline:
            max_island = max(archipelago.island_sizes.values(), default=0)
            if max_island != len(grid) ** 2:
                max_island += 1
            return max_island

        max_island = 0
        for cl_piece in shared_coastline:
            # don't count same island twice; didn't do earlier because
            # islands could've merged
            neighbor_islands = set(island.name for island in cl_piece)
            new_island = sum(
                archipelago.island_sizes[isld] for isld in neighbor_islands
            )
            # one new piece of land added!
            new_island += 1
            if new_island > max_island:
                max_island = new_island

        return max_island


def test():
    sol = Solution()

    cases = [
        (
            {
                "grid": [
                    [1, 0],
                    [0, 1],
                ],
            },
            3,
        ),
        (
            {
                "grid": [
                    [1, 1],
                    [1, 0],
                ]
            },
            4,
        ),
        (
            {
                "grid": [
                    [1, 1],
                    [1, 1],
                ]
            },
            4,
        ),
        (
            {
                "grid": [
                    [0, 0],
                    [0, 0],
                ]
            },
            1,
        ),
        (
            {
                "grid": [
                    [1, 0],
                    [1, 0],
                ]
            },
            3,
        ),
        (
            {
                "grid": [
                    [1, 0, 0, 1, 1],
                    [1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 0],
                ]
            },
            16,
        ),
        (
            {
                "grid": [
                    [1, 0, 0, 0, 1, 0, 1, 0, 1],
                    [0, 1, 0, 0, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 0, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1, 1, 0],
                    [0, 1, 1, 1, 0, 1, 0, 0, 1],
                    [1, 1, 1, 0, 1, 0, 1, 0, 1],
                ]
            },
            34,
        ),
    ]

    for i, (kwargs, expected) in enumerate(cases, 1):
        got = sol.largestIsland(**kwargs)
        assert got == expected, f"case {i} failed: got {got}, expected {expected}"

    print("all tests passed")


if __name__ == "__main__":
    test()
