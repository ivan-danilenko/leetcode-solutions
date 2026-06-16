/*
102. Binary Tree Level Order Traversal
Topic: Tree, Breadth-First Search, Binary Tree
Difficulty: Medium
Status: Solved
Date: 2026-06-08

Key idea:
- BFS.
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
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        queue<TreeNode *> nodes_to_visit;
        if (root != nullptr)
        {
            nodes_to_visit.push(root);
        }
        vector<vector<int>> result;

        // bfs
        while (!nodes_to_visit.empty())
        {
            auto level_size = nodes_to_visit.size();
            result.emplace_back();
            result.back().reserve(level_size);
            for (size_t i{}; i != level_size; ++i)
            {
                auto node = nodes_to_visit.front();
                nodes_to_visit.pop();
                result.back().push_back(node->val);
                if (node->left != nullptr)
                {
                    nodes_to_visit.push(node->left);
                }
                if (node->right != nullptr)
                {
                    nodes_to_visit.push(node->right);
                }
            }
        }

        return result;
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

        size_t i = 1;

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
void printVector(const vector<T> &v)
{
    cout << "[";
    for (int i = 0; i < (int)v.size(); ++i)
    {
        if (i > 0)
            cout << ", ";
        cout << v[i];
    }
    cout << "]";
}

template <typename T>
void printNestedVector(const vector<T> &v)
{
    cout << "[";
    for (int i = 0; i < (int)v.size(); ++i)
    {
        if (i > 0)
            cout << ", ";
        printVector(v[i]);
    }
    cout << "]";
}

template <typename T>
bool sameVector(vector<T> a, vector<T> b, bool ignoreOrder = false)
{
    if (ignoreOrder)
    {
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
    }
    return a == b;
}

template <typename T>
void expectVectorEqual(
    const vector<T> &actual,
    const vector<T> &expected,
    const string &testName,
    bool ignoreOrder = false)
{
    if (sameVector(actual, expected, ignoreOrder))
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: ";
        printVector(expected);
        cout << "\n";
        cout << "  actual:   ";
        printVector(actual);
        cout << "\n";
    }
}

template <typename T>
void sortMembers(
    vector<vector<T>> &v)
{
    for (auto &member : v)
    {
        sort(member.begin(), member.end());
    }
}

template <typename T>
void expectNestedVectorEqual(
    vector<vector<T>> &actual,
    vector<vector<T>> &expected,
    const string &testName,
    bool ignoreInternalOrder = false,
    bool ignoreExternalOrder = false)
{
    if (ignoreInternalOrder)
    {
        sortMembers(actual);
        sortMembers(expected);
    }
    if (sameVector(actual, expected, ignoreExternalOrder))
    {
        cout << "PASS: " << testName << "\n";
    }
    else
    {
        cout << "FAIL: " << testName << "\n";
        cout << "  expected: ";
        printNestedVector(expected);
        cout << "\n";
        cout << "  actual:   ";
        printNestedVector(actual);
        cout << "\n";
    }
}

// -------------------- Main --------------------

int main()
{
    Solution sol;

    {
        Tree tree{{3, 9, 20, nullopt, nullopt, 15, 7}};
        vector<vector<int>> expected{{3}, {9, 20}, {15, 7}};

        auto actual = sol.levelOrder(tree.root);
        expectNestedVectorEqual(actual, expected, "example 1");
    }

    {
        Tree tree{{1}};
        vector<vector<int>> expected{{1}};

        auto actual = sol.levelOrder(tree.root);
        expectNestedVectorEqual(actual, expected, "example 2");
    }

    {
        Tree tree;
        vector<vector<int>> expected;

        auto actual = sol.levelOrder(tree.root);
        expectNestedVectorEqual(actual, expected, "example 3");
    }

    return 0;
}