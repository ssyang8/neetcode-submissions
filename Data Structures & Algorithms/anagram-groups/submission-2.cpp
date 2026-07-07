class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        vector<vector<string>> res;
        for(string s : strs){
            //create a key, key is consist number of occurences of each character
            vector<int> count(26, 0);
            for(char c : s){
                count[c - 'a']++;
            }
            string key = "";
            //need to use #, prevent 1, 1 -> 11, situation to happen
            for(int i = 0; i < count.size(); ++i){
                key += to_string(count[i]) + '#';
            }
            mp[key].push_back(s);
        }
        for(const auto& entry : mp){
            res.push_back(vector<string>(entry.second.begin(), entry.second.end()));
        }
        return res;
    }
};
