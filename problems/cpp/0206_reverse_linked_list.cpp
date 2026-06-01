/*
206. Reverse Linked List
Topic: Linked List, Recursion
Difficulty: Easy
Status: Solved
Date: 2026-06-01

Key idea:
- Use three pointers.
*/

#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *curr = head;
        ListNode *prev = nullptr;
        ListNode *next;
        while (curr != nullptr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
};

// -------------------- Test helpers --------------------

ListNode *makeList(const vector<int> &values)
{
    ListNode dummy;
    ListNode *tail = &dummy;

    for (int x : values)
    {
        tail->next = new ListNode(x);
        tail = tail->next;
    }

    return dummy.next;
}

void deleteList(ListNode *head)
{
    while (head != nullptr)
    {
        ListNode *next = head->next;
        delete head;
        head = next;
    }
}

void printList(ListNode *head)
{
    cout << "[";
    ListNode *node = head;
    while (node->next != nullptr)
    {
        cout << node->val;
        cout << ", ";
        node = node->next;
    }
    cout << node->val;
    cout << "]";
}

bool sameList(ListNode *a, ListNode *b)
{
    while (a != nullptr && b != nullptr)
    {
        if (a->val != b->val)
        {
            return false;
        }

        a = a->next;
        b = b->next;
    }

    return a == b;
}

void expectListEqual(
    ListNode *actual,
    ListNode *expected,
    const string &testName)
{
    if (sameList(actual, expected))
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: ";
        printList(expected);
        cout << "\n";
        cout << "  actual:   ";
        printList(actual);
        cout << "\n";
    }
}

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        vector<int> values = {1, 2, 3, 4, 5};
        auto list = makeList(values);
        vector<int> values_exp = {5, 4, 3, 2, 1};
        auto expected = makeList(values_exp);

        auto actual = sol.reverseList(list);
        expectListEqual(actual, expected, "example 1");
        deleteList(expected);
        // we don't do `deleteList(list);` because nodes are the same as in `expected`
        deleteList(actual);
    }

    {
        vector<int> values = {1, 2};
        auto list = makeList(values);
        vector<int> values_exp = {2, 1};
        auto expected = makeList(values_exp);

        auto actual = sol.reverseList(list);
        expectListEqual(actual, expected, "example 2");
        deleteList(expected);
        // we don't do `deleteList(list);` because nodes are the same as in `expected`
        deleteList(actual);
    }

    {
        vector<int> values = {1};
        auto list = makeList(values);
        vector<int> values_exp = {1};
        auto expected = makeList(values_exp);
        
        auto actual = sol.reverseList(list);
        expectListEqual(actual, expected, "example 3");
        deleteList(expected);
        // we don't do `deleteList(list);` because nodes are the same as in `expected`
        deleteList(actual);
    }

    {
        vector<int> values = {};
        ListNode* list = makeList(values);
        vector<int> values_exp = {};
        ListNode* expected = makeList(values_exp);

        ListNode* actual = sol.reverseList(list);
        expectListEqual(actual, expected, "example 4");
        deleteList(expected);
        // we don't do `deleteList(list);` because nodes are the same as in `expected`
        deleteList(actual);
    }

    return 0;
}