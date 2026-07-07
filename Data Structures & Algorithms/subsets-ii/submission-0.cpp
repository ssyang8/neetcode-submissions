class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    void dfs(vector<int>& nums, int start){
        res.push_back(path);
        for(int i = start; i < nums.size(); ++i){
            if(i > start && nums[i] == nums[i - 1]) continue; // 修改去重逻辑
            path.push_back(nums[i]);
            dfs(nums, i + 1);
            path.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        dfs(nums, 0);
        return res;
    }
};