class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] = -prices[0];  // 持有股票
        dp[0][1] = 0;           // 不持有股票
        
        for (int i = 1; i < n; ++i) {
            if (i >= 2) {
                dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i]);
            } else {
                dp[i][0] = max(dp[i-1][0], -prices[i]);
            }
            
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]);
        }
        
        return dp[n-1][1];
    }
};