class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> st;
        for(int i=0; i<nums.size(); ++i)
        {
            st[nums[i]] = i;
        }
        for(int i=0; i<nums.size(); ++i)
        {
            if(st.find(target-nums[i])!=st.end() && st[target-nums[i]]!=i)
            {

                return {i,st[target-nums[i]]};
            }
        }
        return {0,0};
    }
};
