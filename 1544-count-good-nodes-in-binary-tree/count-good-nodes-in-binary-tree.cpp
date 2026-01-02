/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int goodNodes(TreeNode* root) {
        int count=0;
        dfs(root,root->val,count);
        return count;
    }
    void dfs(TreeNode* node, int maxSoFar, int& count) {
    if (!node) return;

    if (node->val >= maxSoFar) count++;

    maxSoFar = max(maxSoFar, node->val);

    dfs(node->left, maxSoFar, count);
    dfs(node->right, maxSoFar, count);
}

};