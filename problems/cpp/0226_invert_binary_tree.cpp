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
        Tree tree{{4, 2, 7, 1, 3, 6, 9}};
        Tree inv_tree{{4, 7, 2, 9, 6, 3, 1}};
        auto expected = inv_tree.root;

        auto actual = sol.invertTree(tree.root);
        expectEqualTree(actual, expected, "example 1");
    }

    {
        Tree tree{{2, 1, 3}};
        Tree inv_tree{{2, 3, 1}};
        auto expected = inv_tree.root;

        auto actual = sol.invertTree(tree.root);
        expectEqualTree(actual, expected, "example 2");
    }

    {
        Tree tree{{}};
        Tree inv_tree{{}};
        auto expected = inv_tree.root;

        auto actual = sol.invertTree(tree.root);
        expectEqualTree(actual, expected, "example 3");
    }

    return 0;
}