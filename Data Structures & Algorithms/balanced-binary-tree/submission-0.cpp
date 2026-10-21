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
    int traversal(TreeNode* root){
        if(!root) return 0;
        int left = traversal(root->left);
        int right = traversal(root->right);
        if(abs(left-right) > 1) return -1;
        else return 1 + max(left, right);

    }
    bool isBalanced(TreeNode* root) {
        if(traversal(root) == -1) return false;
        return true;
    }
};
