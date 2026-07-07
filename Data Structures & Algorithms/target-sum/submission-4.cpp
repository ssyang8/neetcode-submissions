class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        // pos + neg = target
        // pos - neg = sum
        // target + sum = 2pos
        int sum = 0;
        for(int i=0; i< nums.size(); ++i){
            sum += nums[i];

        }
        int pos = (sum + target)/2;
        if (sum < abs(target) || (sum + target) % 2 != 0) return 0;
        vector<int> dp(pos+1, 0);
        dp[0] = 1;
        for(int i = 0; i < nums.size(); i++){
            for(int j = pos; j >= nums[i]; j--){
                dp[j]+= dp[j-nums[i]];
            }
        }
        return dp[pos];
        
    }
};
