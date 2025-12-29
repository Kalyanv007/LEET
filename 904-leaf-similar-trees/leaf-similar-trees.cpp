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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int>leaves1;
        getLeaves(root1,leaves1);
        vector<int>leaves2;
        getLeaves(root2,leaves2);
        if(leaves1==leaves2){
            return true;
        }
        return false;
    }
    void getLeaves(TreeNode* root, vector<int>& leaves) {
    if (!root) return;

    stack<TreeNode*> st;
    st.push(root);

    while (!st.empty()) {
        TreeNode* node = st.top();
        st.pop();

        if (!node->left && !node->right) {
            leaves.push_back(node->val);
        }

        // Push right first so left is processed first
        if (node->right) st.push(node->right);
        if (node->left) st.push(node->left);
    }
}
};