/*
110. Balanced Binary Tree
Topic: Tree, Depth-First Search, Binary Tree
Difficulty: Easy
Status: Solved
Date: 2026-06-02

Key idea:
- Recursive computation.
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
    bool isBalanced(TreeNode *root)
    {
        return depthIfBalanced(root) >= 0;
    }

private:
    int depthIfBalanced(TreeNode *node)
    {
        // Return `-1` if not balanced.
        if (node == nullptr)
        {
            return 0;
        }
        int left_depth = depthIfBalanced(node->left);
        if (left_depth == -1)
        {
            return -1;
        }
        int right_depth = depthIfBalanced(node->right);
        if (right_depth == -1)
        {
            return -1;
        }
        if (abs(left_depth - right_depth) > 1)
        {
            return -1;
        }
        return max(left_depth, right_depth) + 1;
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
        vector<optional<int>> values = {3, 9, 20, nullopt, nullopt, 15, 7};
        auto tree = makeTree(values);
        auto expected = true;

        auto actual = sol.isBalanced(tree);
        expectEqual(actual, expected, "example 1");
        deleteTree(tree);
    }

    {
        vector<optional<int>> values = {1, 2, 2, 3, 3, nullopt, nullopt, 4, 4};
        auto tree = makeTree(values);
        auto expected = false;

        auto actual = sol.isBalanced(tree);
        expectEqual(actual, expected, "example 2");
        deleteTree(tree);
    }

    {
        vector<optional<int>> values = {};
        auto tree = makeTree(values);
        auto expected = true;

        auto actual = sol.isBalanced(tree);
        expectEqual(actual, expected, "example 3");
        deleteTree(tree);
    }

    return 0;
}