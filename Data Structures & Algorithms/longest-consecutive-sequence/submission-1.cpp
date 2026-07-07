class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        for(int num : nums){
            st.insert(num);
        }
        int res = 0;
        for(int num : nums){
            //first check if the current num is the starting point
            if(!st.count(num - 1)){
                int streak = 1;
                int curNum = num;
                //check if curNum + 1 exist, if it is, curNum++
                while(st.count(curNum + 1)){
                    curNum++;
                    streak++;
                }
                res = max(res, streak);
            }
            
        }
        return res;
    }
};
