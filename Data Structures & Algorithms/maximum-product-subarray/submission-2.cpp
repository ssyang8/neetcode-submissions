class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // dp def: the max product you can get at dp[i], contiguous is lianxude
        vector<int> dp(nums.size(), INT_MIN);
        vector<int> dp_neg(nums.size(), INT_MAX);
        dp[0] = nums[0];
        dp_neg[0] = nums[0];
        int max_ = nums[0];
        for(int i = 1; i < nums.size(); ++i){

            dp_neg[i] = min(nums[i], nums[i]*dp[i-1]);
            dp[i] = max(nums[i], max(nums[i]*dp[i-1], nums[i]*dp_neg[i-1]));

            max_ = max(dp[i], max_);
        }
        return max_;

        
    }
};
