class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    void dfs(vector<int>& nums, vector<bool>& used, int start){
        res.push_back(path);
        for(int i = start; i < nums.size(); ++i){
            if(i > 0 && nums[i] == nums[i - 1]&&used[i - 1] == false) continue;

            path.push_back(nums[i]);
            used[i] = true;
            dfs(nums, used, i+1);
            used[i] = false;
            path.pop_back();
        }

    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<bool> used(nums.size(), false);
        sort(nums.begin(), nums.end());
        dfs(nums, used, 0);
        return res;
    }
};
