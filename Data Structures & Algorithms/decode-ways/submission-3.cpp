class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s[0] == '0') return 0;  // Handle edge case for empty string or leading '0'
        
        vector<int> dp(s.size() + 1, 0);  // dp[i] will store the number of ways to decode the string from index i onwards
        dp[s.size()] = 1;  // Base case: there's one way to decode an empty string (the empty sequence itself)

        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == '0') {
                dp[i] = 0;  // No valid decodings start with '0'
            } else {
                dp[i] = dp[i + 1];  // Single-digit decoding (valid non-'0' characters)
                
                // Check if the next two characters form a valid two-digit decoding (between 10 and 26)
                if (i + 1 < s.size() && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))) {
                    dp[i] += dp[i + 2];  // Add the number of ways to decode from i + 2 onwards (two-digit decoding)
                }
            }
        }

        return dp[0];  // The result is stored at dp[0], which gives the number of ways to decode the full string
    }
};