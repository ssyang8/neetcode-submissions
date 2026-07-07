class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";  // Handle empty string case
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false));
        int length = 0;
        string res = "";
        for (int i = s.size() - 1; i >= 0; --i) {
            for (int j = i; j < s.size(); ++j) {
                if (s[i] == s[j]) {
                    if (j - i < 2) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                    if (dp[i][j] && (j - i + 1 > length)) {
                        length = j - i + 1;
                        res = s.substr(i, j - i + 1);
                    }
                }
            }
        }
        return res;
    }
};