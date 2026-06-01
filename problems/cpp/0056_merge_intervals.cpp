/*
56. Merge Intervals
Topic: Array, Sorting
Difficulty: Medium
Status: Solved
Date: 2026-06-01

Key idea:
- Sort intervals and extend from left to right.
*/

#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        sort(
            intervals.begin(),
            intervals.end());

        vector<vector<int>> result;
        vector<int> current_inter = {intervals[0][0], intervals[0][0]};
        for (auto &inter : intervals)
        {
            if (inter[0] <= current_inter[1])
            {
                current_inter[1] = max(current_inter[1], inter[1]);
            }
            else
            {
                result.push_back(current_inter);
                current_inter = inter;
            }
        }

        result.push_back(current_inter);

        return result;
    }
};

// -------------------- Test helpers --------------------

template <typename T>
void printVector(const vector<T> &v)
{
    cout << "[";
    for (int i = 0; i < (int)v.size(); ++i)
    {
        if (i > 0)
            cout << ", ";
        cout << v[i];
    }
    cout << "]";
}

template <typename T>
void printNestedVector(const vector<T> &v)
{
    cout << "[";
    for (int i = 0; i < (int)v.size(); ++i)
    {
        if (i > 0)
            cout << ", ";
        printVector(v[i]);
    }
    cout << "]";
}

template <typename T>
bool sameVector(vector<T> a, vector<T> b, bool ignoreOrder = false)
{
    if (ignoreOrder)
    {
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
    }
    return a == b;
}

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

template <typename T>
void expectVectorEqual(
    const vector<T> &actual,
    const vector<T> &expected,
    const string &testName,
    bool ignoreOrder = false)
{
    if (sameVector(actual, expected, ignoreOrder))
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: ";
        printVector(expected);
        cout << "\n";
        cout << "  actual:   ";
        printVector(actual);
        cout << "\n";
    }
}

template <typename T>
void sortMembers(
    vector<vector<T>> &v)
{
    for (auto &member : v)
    {
        sort(member.begin(), member.end());
    }
}

template <typename T>
void expectNestedVectorEqual(
    vector<vector<T>> &actual,
    vector<vector<T>> &expected,
    const string &testName,
    bool ignoreInternalOrder = false,
    bool ignoreExternalOrder = false)
{
    if (ignoreInternalOrder)
    {
        sortMembers(actual);
        sortMembers(expected);
    }
    if (sameVector(actual, expected, ignoreExternalOrder))
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: ";
        printNestedVector(expected);
        cout << "\n";
        cout << "  actual:   ";
        printNestedVector(actual);
        cout << "\n";
    }
}

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<vector<int>> nums = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
        vector<vector<int>> expected = {{1, 6}, {8, 10}, {15, 18}};

        auto actual = sol.merge(nums);
        expectNestedVectorEqual(actual, expected, "example 1", false, true);
    }

    {
        vector<vector<int>> nums = {{1, 4}, {4, 5}};
        vector<vector<int>> expected = {{1, 5}};

        auto actual = sol.merge(nums);
        expectNestedVectorEqual(actual, expected, "example 2", false, true);
    }

    {
        vector<vector<int>> nums = {{4, 7}, {1, 7}};
        vector<vector<int>> expected = {{1, 7}};

        auto actual = sol.merge(nums);
        expectNestedVectorEqual(actual, expected, "example 3", false, true);
    }

    {
        vector<vector<int>> nums = {{1, 7}, {4, 5}};
        vector<vector<int>> expected = {{1, 7}};

        auto actual = sol.merge(nums);
        expectNestedVectorEqual(actual, expected, "example 4", false, true);
    }

    return 0;
}