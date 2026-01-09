class Solution {
public:
    // Returns {subtreeRoot, depth}
    pair<TreeNode*, int> dfs(TreeNode* root) {
        if (!root) return {nullptr, 0};

        auto left = dfs(root->left);
        auto right = dfs(root->right);

        // If left subtree is deeper
        if (left.second > right.second) {
            return {left.first, left.second + 1};
        }

        // If right subtree is deeper
        if (right.second > left.second) {
            return {right.first, right.second + 1};
        }

        // If both sides are equally deep
        return {root, left.second + 1};
    }

    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        return dfs(root).first;
    }
};
