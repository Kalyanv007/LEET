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
    int maxPathSum(TreeNode* root) {
        int sum=INT_MIN;
        maxPathDown(root,sum);
        return sum;

    }
    int maxPathDown(TreeNode* root,int &sum){
        if(root==NULL)return 0;
        int leftsum=max(0,maxPathDown(root->left,sum));
        int rightsum=max(0,maxPathDown(root->right,sum));
        sum=max(sum,leftsum+rightsum+root->val);
        return max(leftsum,rightsum)+root->val;
    }
};