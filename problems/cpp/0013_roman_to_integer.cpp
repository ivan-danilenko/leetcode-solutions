/*
13. Roman to Integer
Topic: Hash Table, Math, String
Difficulty: Easy
Status: Solved
Date: 2026-05-29

Key idea:
- Iterate from the end.
*/

#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        unordered_map<char, int> literal_conversion = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}};

        int result = 0;
        int last_max_literal_value = 0;
        int literal_value;
        for (auto it = s.rbegin(); it != s.rend(); it++)
        {
            literal_value = literal_conversion[*it];
            if (literal_value > last_max_literal_value)
            {
                last_max_literal_value = literal_value;
            }
            if (literal_value < last_max_literal_value)
            {
                result -= literal_value;
            }
            else
            {
                result += literal_value;
            }
        }

        return result;
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
        const string s = "III";
        const int expected = 3;

        auto actual = sol.romanToInt(s);
        expectEqual(actual, expected, "example 1");
    }

    {
        const string s = "LVIII";
        const int expected = 58;

        auto actual = sol.romanToInt(s);
        expectEqual(actual, expected, "example 2");
    }

    {
        const string s = "MCMXCIV";
        const int expected = 1994;

        auto actual = sol.romanToInt(s);
        expectEqual(actual, expected, "example 3");
    }

    return 0;
}