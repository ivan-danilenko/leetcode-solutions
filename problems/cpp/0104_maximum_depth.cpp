/*
104. Maximum Depth of Binary Tree
Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Difficulty: Easy
Status: Solved
Date: 2026-06-02

Key idea:
- Recursive computation.
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
    int maxDepth(TreeNode *root)
    {
        if (root == nullptr)
        {
            return 0;
        }
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

// -------------------- Test helpers --------------------

// to create a tree without a need for explicit destruction call
class Tree
{
public:
    TreeNode *root = nullptr;

    Tree() = default;

    Tree(const vector<optional<int>> &values)
    {
        if (values.empty() || !values[0].has_value())
        {
            return;
        }
        nodes.reserve(values.size());

        root = makeNode(values[0].value());

        queue<TreeNode *> q;
        q.push(root);

        size_t i{1};

        while (!q.empty() && i < values.size())
        {
            TreeNode *curr = q.front();
            q.pop();

            if (i < values.size() && values[i].has_value())
            {
                curr->left = makeNode(values[i].value());
                q.push(curr->left);
            }
            ++i;

            if (i < values.size() && values[i].has_value())
            {
                curr->right = makeNode(values[i].value());
                q.push(curr->right);
            }
            ++i;
        }
    }

private:
    vector<unique_ptr<TreeNode>> nodes;

    TreeNode *makeNode(int val)
    {
        nodes.push_back(make_unique<TreeNode>(val));
        return nodes.back().get();
    }
};

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
        Tree tree = {{3, 9, 20, nullopt, nullopt, 15, 7}};
        auto expected = 3;

        auto actual = sol.maxDepth(tree.root);
        expectEqual(actual, expected, "example 1");
    }

    {
        Tree tree = {{1, nullopt, 2}};
        auto expected = 2;

        auto actual = sol.maxDepth(tree.root);
        expectEqual(actual, expected, "example 2");
    }

    return 0;
}