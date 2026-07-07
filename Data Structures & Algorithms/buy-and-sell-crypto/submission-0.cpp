class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int ans = 0;
        for(int right = 1; right < prices.size(); ++right)
        {
            ans = max(ans, prices[right] - prices[left]);
            if(prices[right] < prices[left]) left = right; 
        }

        return ans;
    }
};
