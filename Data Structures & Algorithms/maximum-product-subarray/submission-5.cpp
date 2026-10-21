class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int curMin = 1, curMax = 1;

        for (int n : nums) {
            int tmp = curMax * n;
            curMax = max(n * curMax, n * curMin);
            curMin = min(tmp, n * curMin);
            res = max(res, curMax);
        }
        return res;
    }
};
