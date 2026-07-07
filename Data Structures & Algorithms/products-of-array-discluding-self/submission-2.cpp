class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix = 1;
        vector<int> prefixV(nums.size(), 1);
        for(int i = 0; i < nums.size(); ++i){
            prefixV[i] = prefix;
            prefix *= nums[i];
        }

        int pofix = 1;
        vector<int> res(nums.size(), 1);
        for(int i = nums.size() - 1; i >= 0; --i){
            res[i] = pofix * prefixV[i];
            pofix *= nums[i];
        }
        return res;
    }
};
