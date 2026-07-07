class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    void dfs(vector<int>& nums, int start){
        res.push_back(path);
        if(start >= nums.size()){
            return;
        }
        for(int i = start; i < nums.size(); ++i){
            path.push_back(nums[i]);
            dfs(nums, i+1);
            path.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(nums, 0);
        return res;
    }
};
