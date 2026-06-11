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

// to create a tree without a need for explicit destruction call
class List
{
public:
    ListNode *head = nullptr;

    List() = default;

    List(const vector<int> &values)
    {
        ListNode dummy;
        ListNode *tail = &dummy;

        for (int x : values)
        {
            tail->next = makeNode(x);
            tail = tail->next;
        }

        this->head = dummy.next;
    }

private:
    vector<unique_ptr<ListNode>> nodes;

    ListNode *makeNode(int val)
    {
        nodes.push_back(make_unique<ListNode>(val));
        return nodes.back().get();
    }
};

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
        List list{{1, 2, 3, 4, 5}};
        List rev_list{{5, 4, 3, 2, 1}};
        auto expected = rev_list.head;

        auto actual = sol.reverseList(list.head);
        expectListEqual(actual, expected, "example 1");
    }

    {
        List list{{1, 2}};
        List rev_list{{2, 1}};
        auto expected = rev_list.head;

        auto actual = sol.reverseList(list.head);
        expectListEqual(actual, expected, "example 2");
    }

    {
        List list{{1}};
        List rev_list{{1}};
        auto expected = rev_list.head;

        auto actual = sol.reverseList(list.head);
        expectListEqual(actual, expected, "example 3");
    }

    {
        List list;
        List rev_list;
        auto expected = rev_list.head;

        auto actual = sol.reverseList(list.head);
        expectListEqual(actual, expected, "example 4");
    }

    return 0;
}