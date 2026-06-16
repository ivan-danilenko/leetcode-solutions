/*
3. Longest Substring Without Repeating Characters
Topic: Staff, Hash Table, String, Sliding Window
Difficulty: Medium
Status: Solved
Date: 2026-06-16

Key idea:
- Sliding window.
*/

#include <string>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> last_seen;
        size_t max_length{};
        size_t curr_length{};
        const size_t n_printable_ascii_chars{92};
        last_seen.reserve(min(s.length(), n_printable_ascii_chars));
        for (size_t i{}; i < s.length(); ++i)
        {
            auto ch = s[i];
            if (last_seen.find(ch) == last_seen.end())
            {
                last_seen[ch] = i;
                ++curr_length;
            }
            else
            {
                max_length = max(max_length, curr_length);
                curr_length = min(curr_length + 1, i - last_seen[ch]);
                last_seen[ch] = i;
            }
        }
        max_length = max(max_length, curr_length);

        return max_length;
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
        string s{"abcabcbb"};
        int expected{3};

        auto actual = sol.lengthOfLongestSubstring(s);
        expectEqual(actual, expected, "example 1");
    }

    {
        string s{"bbbbb"};
        int expected{1};

        auto actual = sol.lengthOfLongestSubstring(s);
        expectEqual(actual, expected, "example 2");
    }

    {
        string s{"pwwkew"};
        int expected{3};

        auto actual = sol.lengthOfLongestSubstring(s);
        expectEqual(actual, expected, "example 3");
    }

    {
        string s{"dvdf"};
        int expected{3};

        auto actual = sol.lengthOfLongestSubstring(s);
        expectEqual(actual, expected, "example 4");
    }

    {
        string s{"tmmzuxt"};
        int expected{5};

        auto actual = sol.lengthOfLongestSubstring(s);
        expectEqual(actual, expected, "example 5");
    }

    return 0;
}