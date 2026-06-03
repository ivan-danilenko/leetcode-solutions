/*
226. Invert Binary Tree
Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Difficulty: Easy
Status: Solved
Date: 2026-06-02

Key idea:
- Recursive inversion.
*/

#include <iostream>
#include <optional>
#include <utility>
#include <queue>
#include <cstdlib>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    TreeNode *invertTree(TreeNode *root)
    {
        if (root)
        {
            invertTree(root->left);
            invertTree(root->right);
            swap(root->left, root->right);
        }

        return root;
    }
};

// -------------------- Test helpers --------------------

TreeNode *makeTree(const vector<optional<int>> &values)
{
    if (values.empty() || !values[0].has_value())
    {
        return nullptr;
    }

    TreeNode *root = new TreeNode(values[0].value());
    queue<TreeNode *> q;
    q.push(root);

    size_t i = 1;

    while (!q.empty() && i < values.size())
    {
        TreeNode *curr = q.front();
        q.pop();

        // left child
        if (i < values.size() && values[i].has_value())
        {
            curr->left = new TreeNode(values[i].value());
            q.push(curr->left);
        }
        ++i;

        // right child
        if (i < values.size() && values[i].has_value())
        {
            curr->right = new TreeNode(values[i].value());
            q.push(curr->right);
        }
        ++i;
    }

    return root;
}

void deleteTree(TreeNode *root)
{
    if (root == nullptr)
    {
        return;
    }

    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

bool sameTree(TreeNode *p, TreeNode *q)
{
    if (p == nullptr || q == nullptr)
    {
        return p == q;
    }
    return (p->val == q->val && sameTree(p->left, q->left) && sameTree(p->right, q->right));
}

void expectEqualTree(TreeNode *actual, TreeNode *expected, const string &testName)
{
    if (sameTree(actual, expected))
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
        vector<optional<int>> values1 = {4, 2, 7, 1, 3, 6, 9};
        auto tree = makeTree(values1);
        vector<optional<int>> values2 = {4, 7, 2, 9, 6, 3, 1};
        auto expected = makeTree(values2);

        auto actual = sol.invertTree(tree);
        expectEqualTree(actual, expected, "example 1");
        deleteTree(tree);
        deleteTree(expected);
    }

    {
        vector<optional<int>> values1 = {2, 1, 3};
        auto tree = makeTree(values1);
        vector<optional<int>> values2 = {2, 3, 1};
        auto expected = makeTree(values2);

        auto actual = sol.invertTree(tree);
        expectEqualTree(actual, expected, "example 2");
        deleteTree(tree);
        deleteTree(expected);
    }

    {
        vector<optional<int>> values1 = {};
        auto tree = makeTree(values1);
        vector<optional<int>> values2 = {};
        auto expected = makeTree(values2);

        auto actual = sol.invertTree(tree);
        expectEqualTree(actual, expected, "example 3");
        deleteTree(tree);
        deleteTree(expected);
    }

    return 0;
}