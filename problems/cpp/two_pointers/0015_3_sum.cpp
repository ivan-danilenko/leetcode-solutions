/*
15. 3 Sum
Topic: Array, Two Pointers, Sorting
Difficulty: Medium
Status: Solved
Date: 2026-05-28

Key idea:
- Two pointers for each third value.
*/

#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        int first = 0;
        while (first < (int)nums.size() - 2)
        {
            if (nums[first] + nums[first + 1] + nums[first + 2] > 0)
            {
                break;
            }
            int left = first + 1, right = nums.size() - 1;
            auto target = -nums[first];
            while (left < right)
            {
                int sum = nums[left] + nums[right];
                if (sum == target)
                {
                    result.push_back({nums[first], nums[left], nums[right]});

                    auto nums_left = nums[left];
                    while (left < right && nums[left] == nums_left)
                    {
                        left++;
                    }
                    auto nums_right = nums[right];
                    while (left < right && nums[right] == nums_right)
                    {
                        right--;
                    }
                }
                else if (sum > target)
                {
                    auto nums_right = nums[right];
                    while (left < right && nums[right] == nums_right)
                    {
                        right--;
                    }
                }
                else
                {
                    auto nums_left = nums[left];
                    while (left < right && nums[left] == nums_left)
                    {
                        left++;
                    }
                }
            }

            auto nums_first = nums[first];
            while (first < (int)nums.size() && nums[first] == nums_first)
            {
                first++;
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
        vector<int> nums = {-1, 0, 1, 2, -1, -4};
        // vector<vector<int>> expected = {{-1, -1, 2}, {-1, 0, 1}};
        vector<vector<int>> expected = {{-1, 0, 1}, {2, -1, -1}};

        auto actual = sol.threeSum(nums);
        expectNestedVectorEqual(actual, expected, "example 1", true, true);
    }

    {
        vector<int> nums = {0, 1, 1};
        vector<vector<int>> expected;

        auto actual = sol.threeSum(nums);
        expectNestedVectorEqual(actual, expected, "example 2", true, true);
    }

    {
        vector<int> nums = {0, 0, 0};
        vector<vector<int>> expected = {{0, 0, 0}};

        auto actual = sol.threeSum(nums);
        expectNestedVectorEqual(actual, expected, "example 3", true, true);
    }

    {
        vector<int> nums = {-100, -70, -60, 110, 120, 130, 160};
        vector<vector<int>> expected = {{-100, -60, 160}, {-70, -60, 130}};

        auto actual = sol.threeSum(nums);
        expectNestedVectorEqual(actual, expected, "example 4", true, true);
    }

    return 0;
}