class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for(int i = 0; i < nums.size(); ++i){
            sum += nums[i];
        }
        if(sum % 2 != 0) return false;
        int bagSize = sum/2;
        vector<int> dp(10001, 0);
        for(int i = 0; i < nums.size(); i++) {
            for(int j = bagSize; j >= nums[i]; j--) {
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);
            }
        }
        if (dp[bagSize] == bagSize) return true;
        return false;

    }
};
