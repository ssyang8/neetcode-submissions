class Solution {
public:
    int numDecodings(string s) {
        vector<int> dp(s.size(), 1);
        for(int i = s.size() - 1; i >= 0; --i){
            if(s[i] == '0') dp[i] = 0;
            else{
                if(i+1 < s.size()){
                    dp[i] = dp[i+1] + 1;
                }

            }
        }
        return dp[0];
    }
};