/*
100. Same Tree
Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Difficulty: Easy
Status: Solved
Date: 2026-06-02

Key idea:
- Recursive check.
*/

#include <iostream>
#include <optional>
#include <queue>
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
    bool isSameTree(TreeNode *p, TreeNode *q)
    {
        if (p == nullptr || q == nullptr)
        {
            return p == q;
        }
        return (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
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
        vector<optional<int>> values1 = {1, 2, 3};
        auto tree1 = makeTree(values1);
        vector<optional<int>> values2 = {1, 2, 3};
        auto tree2 = makeTree(values2);
        auto expected = true;

        auto actual = sol.isSameTree(tree1, tree2);
        expectEqual(actual, expected, "example 1");
        deleteTree(tree1);
        deleteTree(tree2);
    }

    {
        vector<optional<int>> values1 = {1, 2};
        auto tree1 = makeTree(values1);
        vector<optional<int>> values2 = {1, nullopt, 2};
        auto tree2 = makeTree(values2);
        auto expected = false;

        auto actual = sol.isSameTree(tree1, tree2);
        expectEqual(actual, expected, "example 2");
        deleteTree(tree1);
        deleteTree(tree2);
    }

    {
        vector<optional<int>> values1 = {1, 2, 1};
        auto tree1 = makeTree(values1);
        vector<optional<int>> values2 = {1, 1, 2};
        auto tree2 = makeTree(values2);
        auto expected = false;

        auto actual = sol.isSameTree(tree1, tree2);
        expectEqual(actual, expected, "example 3");
        deleteTree(tree1);
        deleteTree(tree2);
    }

    return 0;
}