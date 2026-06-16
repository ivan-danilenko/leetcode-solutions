/*
20. Valid Parentheses
Topic: String, Stack
Difficulty: Easy
Status: Solved
Date: 2026-05-29

Key idea:
- Keep opening parentheses in a stack.
*/

#include <string>
#include <iostream>
#include <stack>
using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> open;
        char expected_parenthesis;
        for (auto it = s.begin(); it != s.end(); it++)
        {
            switch (*it)
            {
            case '(':
            case '[':
            case '{':
                open.push(*it);
                continue;
            case ')':
                expected_parenthesis = '(';
                break;
            case ']':
                expected_parenthesis = '[';
                break;
            case '}':
                expected_parenthesis = '{';
                break;
            }
            if (open.empty() || open.top() != expected_parenthesis)
            {
                return false;
            }
            open.pop();
        }

        return open.empty();
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
        const string s = "()";
        const bool expected = true;

        auto actual = sol.isValid(s);
        expectEqual(actual, expected, "example 1");
    }
    {
        const string s = "()[]{}";
        const bool expected = true;

        auto actual = sol.isValid(s);
        expectEqual(actual, expected, "example 2");
    }
    {
        const string s = "(]";
        const bool expected = false;

        auto actual = sol.isValid(s);
        expectEqual(actual, expected, "example 3");
    }
    {
        const string s = "([])";
        const bool expected = true;

        auto actual = sol.isValid(s);
        expectEqual(actual, expected, "example 4");
    }
    {
        const string s = "([)]";
        const bool expected = false;

        auto actual = sol.isValid(s);
        expectEqual(actual, expected, "example 5");
    }
    {
        const string s = "]";
        const bool expected = false;

        auto actual = sol.isValid(s);
        expectEqual(actual, expected, "example 6");
    }
    {
        const string s = "(";
        const bool expected = false;

        auto actual = sol.isValid(s);
        expectEqual(actual, expected, "example 7");
    }

    return 0;
}