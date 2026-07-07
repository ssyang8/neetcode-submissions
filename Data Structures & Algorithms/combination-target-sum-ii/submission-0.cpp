class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    void dfs(vector<int>& candidates, int target, int sum, int start, vector<bool>& used){
        if(sum == target){
            res.push_back(path);
            return;
        }
        for(int i = start; i < candidates.size(); ++i){
            if(i > 0 && candidates[i] == candidates[i-1] && used[i - 1] == false) continue;
            path.push_back(candidates[i]);
            sum+=candidates[i];
            used[i] = true;
            dfs(candidates, target, sum, i+1, used);
            path.pop_back();
            sum-=candidates[i];
            used[i] = false;
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<bool> used(candidates.size(), false);
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, 0, used);
        return res;
    }
};
