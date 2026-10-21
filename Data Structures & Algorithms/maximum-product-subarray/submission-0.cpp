class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // dp def: the max product you can get at dp[i], contiguous is lianxude
        vector<int> dp(nums.size(), INT_MIN);
        dp[0] = nums[0];
        int max_ = INT_MIN;
        for(int i = 1; i < nums.size(); ++i){
            dp[i] = max(nums[i], nums[i]*dp[i-1]);
            max_ = max(dp[i], max_);
        }
        return max_;

        
    }
};
