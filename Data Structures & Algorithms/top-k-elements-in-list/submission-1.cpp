class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
                //bucket sort
        vector<vector<int>> buckets(nums.size() + 1);
        unordered_map<int, int> mp;
        for(int num : nums){
            mp[num]++;
        }
        for(const auto& entry : mp){
            buckets[entry.second].push_back(entry.first);
        }
        vector<int> res;

        for(int i = buckets.size() - 1; i >= 0; --i){
             while(res.size() < k && !buckets[i].empty()){
                res.push_back(buckets[i].back());
                buckets[i].pop_back();

             }
            
        }
        return res;
    }
};
