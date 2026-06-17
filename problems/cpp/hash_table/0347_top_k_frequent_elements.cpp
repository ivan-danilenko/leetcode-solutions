/*
347. Top K Frequent Elements
Topic: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue),
  Bucket Sort, Counting, Quickselect
Difficulty: Medium
Status: Solved
Date: 2026-06-17

Key idea:
- Store frequencies in a hashmap,
- Use a heap to find largest `k` frequencies.
*/

#include <vector>
#include <unordered_map>
#include <iostream>
#include <queue>
#include <utility>
#include <exception>
using namespace std;

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> frequencies;
        for (auto n : nums)
        {
            ++frequencies[n];
        }

        vector<int> nums_no_repeat(frequencies.size());
        size_t index{};
        for (auto [n, freq] : frequencies)
        {
            nums_no_repeat[index] = n;
            ++index;
        }

        auto comp = [&frequencies](int x, int y)
        { return frequencies[x] < frequencies[y]; };

        priority_queue<int, vector<int>, decltype(comp)> heap(comp, std::move(nums_no_repeat));

        vector<int> result(k);
        for (int i{}; i < k; ++i)
        {
            result[i] = heap.top();
            heap.pop();
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

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<int> nums = {1, 1, 1, 2, 2, 3};
        int k = 2;
        vector<int> expected = {1, 2};

        auto actual = sol.topKFrequent(nums, k);
        expectVectorEqual(actual, expected, "example 1", true);
    }

    {
        vector<int> nums = {1};
        int k = 1;
        vector<int> expected = {1};

        auto actual = sol.topKFrequent(nums, k);
        expectVectorEqual(actual, expected, "example 2", true);
    }

    {
        vector<int> nums = {1, 2, 1, 2, 1, 2, 3, 1, 3, 2};
        int k = 2;
        vector<int> expected = {1, 2};

        auto actual = sol.topKFrequent(nums, k);
        expectVectorEqual(actual, expected, "example 3", true);
    }

    return 0;
}