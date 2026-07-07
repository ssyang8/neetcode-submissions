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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        deque<TreeNode*> q;
        q.push_back(root);
        if(!root) return res;
        while(!q.empty()){
            int len = q.size();
            for(int i = 0; i < len; ++i ){
                TreeNode* node = q.front();
                q.pop_front();
                if(node->left) q.push_back(node->left);
                if(node->right) q.push_back(node->right);
                if(i == len - 1){
                    res.push_back(node->val);
                }
            }
        }
        return res;
    }
};
