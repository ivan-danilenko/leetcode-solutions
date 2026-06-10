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
        Tree tree1{{1, 2, 3}};
        Tree tree2{{1, 2, 3}};
        auto expected = true;

        auto actual = sol.isSameTree(tree1.root, tree2.root);
        expectEqual(actual, expected, "example 1");
    }

    {
        Tree tree1{{1, 2}};
        Tree tree2{{1, nullopt, 2}};
        auto expected = false;

        auto actual = sol.isSameTree(tree1.root, tree2.root);
        expectEqual(actual, expected, "example 2");
    }

    {
        Tree tree1{{1, 2, 1}};
        Tree tree2{{1, 1, 2}};
        auto expected = false;

        auto actual = sol.isSameTree(tree1.root, tree2.root);
        expectEqual(actual, expected, "example 3");
    }

    return 0;
}