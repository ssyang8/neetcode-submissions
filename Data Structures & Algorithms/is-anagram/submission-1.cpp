class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        unordered_set<char> s_st;
        if(s.size()!=t.size()) return false;
        for(int i=0; i<s.size(); i++)
        {
            s_st.insert(s[i]);
        }
        for(int i=0; i<t.size(); ++i)
        {
            if(s_st.find(t[i]) == s_st.end())
            {
                return false;
            }
        }
        return true;
    }
};
