class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> st;
        int l = 0;
        int res = 0;
        for(int r = 0; r < s.size(); ++r){
            while(st.count(s[r])){
                st.erase(s[l++]);

            }
            st.insert(s[r]);
            res = max(r - l + 1, res);

        }
        return res;
    }
};
