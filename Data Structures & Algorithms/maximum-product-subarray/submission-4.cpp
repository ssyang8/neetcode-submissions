class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int curMin = 1, curMax = 1;

        for (int n : nums) {
            int tmp = curMax * n;
            curMax = max(max(n * curMax, n * curMin), n);
            curMin = min(min(tmp, n * curMin), n);
            res = max(res, curMax);
        }
        return res;
    }
};
