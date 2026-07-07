class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        if (n < 2) return 0;  // 处理边界情况

        vector<int> dp(n);
        dp[0] = cost[0];
        dp[1] = cost[1];

        for(int i = 2; i < n; ++i){
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i];
        }

        return min(dp[n-1], dp[n-2]);  // 返回到达楼顶的最小花费
    }
};
