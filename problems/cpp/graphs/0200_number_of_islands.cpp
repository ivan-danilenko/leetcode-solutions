/*
200. Number of Islands
Topic: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
Difficulty: Medium
Status: Solved
Date: 2026-06-17

Key idea:
- Every time you see an island to dfs/bfs to mark the island.
*/

#include <iostream>
using namespace std;

class Solution
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        int number_of_islands{};
        for (size_t r{}; r < grid.size(); ++r)
        {
            for (size_t c{}; c < grid[r].size(); ++c)
            {
                if (grid[r][c] == '1')
                {
                    ++number_of_islands;
                    mark_dfs(r, c, grid);
                }
            }
        }

        return number_of_islands;
    }

private:
    void mark_dfs(const size_t r, const size_t c, vector<vector<char>> &grid)
    {
        if (grid[r][c] != '1')
            return;

        grid[r][c] = '*';
        if (r > 0)
        {
            mark_dfs(r - 1, c, grid);
        }
        if (c > 0)
        {
            mark_dfs(r, c - 1, grid);
        }
        if (r + 1 < grid.size())
        {
            mark_dfs(r + 1, c, grid);
        }
        if (c + 1 < grid[r].size())
        {
            mark_dfs(r, c + 1, grid);
        }
    }
};

// -------------------- Test helpers --------------------

template <typename T>
void expectEqual(const T &actual, const T &expected, const string &testName)
{
    if (actual == expected)
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: " << expected << "\n";
        cout << "  actual:   " << actual << "\n";
    }
}

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<vector<char>> grid{
            {'1', '1', '1', '1', '0'},
            {'1', '1', '0', '1', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '0', '0', '0'}};
        const int expected = 1;

        auto actual = sol.numIslands(grid);
        expectEqual(actual, expected, "example 1");
    }

    {
        vector<vector<char>> grid{
            {'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'}};
        const int expected = 3;

        auto actual = sol.numIslands(grid);
        expectEqual(actual, expected, "example 2");
    }

    return 0;
}