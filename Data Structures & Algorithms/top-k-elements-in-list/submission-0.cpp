class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        unordered_map<int,int> count;
        vector<vector<int>> frq(nums.size() + 1);
        for(int& it : nums)
        {
            count[it]++;
        }
        for(auto& it : count)
        {
            frq[it.second].push_back(it.first);
        }
        vector<int> res;
        for(int i = frq.size()-1; i>0; --i)
        {
            for(int n: frq[i])
            {
                res.push_back(n);
                if(res.size() == k)
                {
                    return res;
                }
            }
        }
        return res;
    }
};
