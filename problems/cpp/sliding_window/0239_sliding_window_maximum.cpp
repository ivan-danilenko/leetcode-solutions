/*
239. Sliding Window Maximum
Topic: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
Difficulty: Hard
Status: Solved
Date: 2026-06-17

Key idea:
- Keep track of profile of the sequence as seen from the right. I.e.
  for every level we should be able to find when was the last time we
  have seen this height or higher.
- To achive this monotonic deque `pivot_indices` of indices. The values of
`nums` at these indices are increasing and indices themselves are decreasing.
- We drop the indices outside of the window.
*/

#include <vector>
#include <deque>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        deque<int> pivot_indices;
        vector<int> result(nums.size() - k + 1);
        const int n{static_cast<int>(nums.size())};

        for (int i{}; i < n; ++i)
        {
            if (!pivot_indices.empty() && pivot_indices.back() <= i - k)
            {
                pivot_indices.pop_back();
            }
            while (!pivot_indices.empty() && nums[pivot_indices.front()] <= nums[i])
            {
                pivot_indices.pop_front();
            }

            pivot_indices.push_front(i);

            if (i >= k - 1)
            {
                result[i - k + 1] = nums[pivot_indices.back()];
            }
        }

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

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<int> nums{1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        vector<int> expected{3, 3, 5, 5, 6, 7};

        auto actual = sol.maxSlidingWindow(nums, k);
        expectVectorEqual(actual, expected, "example 1");
    }

    {
        vector<int> nums{1};
        int k = 1;
        vector<int> expected{1};

        auto actual = sol.maxSlidingWindow(nums, k);
        expectVectorEqual(actual, expected, "example 2");
    }

    {
        vector<int> nums{2, 0, 1, 0};
        int k = 3;
        vector<int> expected{2, 1};

        auto actual = sol.maxSlidingWindow(nums, k);
        expectVectorEqual(actual, expected, "example 3");
    }

    return 0;
}