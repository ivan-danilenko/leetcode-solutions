/*
101. Symmetric Tree
Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Difficulty: Easy
Status: Solved
Date: 2026-06-02

Key idea:
- Compare two branches similar to 100.
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
    bool isSymmetric(TreeNode *root)
    {
        return isMirror(root->left, root->right);
    }

private:
    bool isMirror(TreeNode *p, TreeNode *q)
    {
        if (p == nullptr || q == nullptr)
        {
            return p == q;
        }
        return (p->val == q->val && isMirror(p->left, q->right) && isMirror(p->right, q->left));
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
        vector<optional<int>> values = {1, 2, 2, 3, 4, 4, 3};
        auto tree = makeTree(values);
        auto expected = true;

        auto actual = sol.isSymmetric(tree);
        expectEqual(actual, expected, "example 1");
        deleteTree(tree);
    }

    {
        vector<optional<int>> values = {1, 2, 2, nullopt, 3, nullopt, 3};
        auto tree = makeTree(values);
        auto expected = false;

        auto actual = sol.isSymmetric(tree);
        expectEqual(actual, expected, "example 2");
        deleteTree(tree);
    }

    return 0;
}