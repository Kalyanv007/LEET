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
    int maxLevelSum(TreeNode* root) {
        int level=1;
        queue<TreeNode*>q;
        int maxSum=INT_MIN;
        int maxLevel=1;
        q.push(root);
        while(!q.empty()){
            int size=q.size();
            int curr_sum=0;
            for(int i=0;i<size;i++){
                TreeNode* node=q.front();
                q.pop();
                curr_sum+=node->val;
                if(node->left!=NULL)q.push(node->left);
                if(node->right!=NULL)q.push(node->right);
            }
            if(curr_sum>maxSum){
                maxLevel=level;
                maxSum=curr_sum;
            }
            level++;
        }
        return maxLevel;
    }
    // vector<vector<int>> levelOrder(TreeNode* root) {
    //     vector<vector<int>>ans;
    //     if(root==NULL)return ans;
    //     queue<TreeNode*> q;
    //     q.push(root);
    //     while(!q.empty()){
    //         int size=q.size();
    //         vector<int>level;
    //         for(int i=0;i<size;i++){
    //             TreeNode* node=q.front();
    //             q.pop();
    //             if(node->left!=NULL)q.push(node->left);
    //             if(node->right!=NULL)q.push(node->right);
    //             level.push_back(node->val);
    //         }
    //         ans.push_back(level);
    //     }
    //     return ans;
    // }
};