class Solution {
public:
    int jump(vector<int>& nums) {
        if(nums.size() == 1) return 0;
        int curDis = 0;
        int nextDis = 0;
        int step = 0;
        for(int i = 0; i < nums.size(); ++i){
            nextDis = max(nextDis, i + nums[i]);
            if(i == curDis){
                curDis = nextDis;
                step++;
                if (nextDis >= nums.size() - 1) break; 
            }
        }
        return step;

    }
};