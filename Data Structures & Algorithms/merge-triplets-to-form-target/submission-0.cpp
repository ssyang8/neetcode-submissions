class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        int count = 0;
        vector<int> maxTriplet(3, 0);
        for(auto& t : triplets){
            if(t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                for(int i = 0; i < 3; ++i){
                    maxTriplet[i] = max(maxTriplet[i], t[i]);
                }
            }
        }
        return maxTriplet == target;
    }
};