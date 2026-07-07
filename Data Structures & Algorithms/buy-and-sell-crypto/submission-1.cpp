class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 初始化变量
        int left = 0; // 窗口左端：记录最低买入价格的位置
        int right = 0; // 窗口右端：用于遍历价格数组
        int maxProfit = 0; // 最大利润
        
        while (right < prices.size()) {
            // 如果发现更低的买入价格，就移动左窗口
            if (prices[right] < prices[left]) {
                left = right;
            }
            
            // 计算当前利润，并更新最大利润
            int profit = prices[right] - prices[left];
            maxProfit = max(maxProfit, profit);
            
            // 移动右窗口
            right++;
        }
        
        return maxProfit;
    }
};