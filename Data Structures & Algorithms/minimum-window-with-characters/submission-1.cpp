class Solution {
public:
    string minWindow(string s, string t) {
        //check if char in the window 符合 t
        int valid = 0;
        unordered_map<char, int> need, window;
        //check the requirement of t
        for(char c : t){
            need[c]++;
        }
        int l = 0;
        int start = 0;
        int len = INT_MAX;
        for(int r = 0; r < s.size(); ++r){
            char c = s[r];
            if(need.count(c)){
                window[c]++;
                //if one character c  accord with need[c], valid++
                if(window[c] == need[c]){
                    valid++;
                }
            }
            //if valid == need.size(), meaning there is already result in the window, try to move l
            while(valid == need.size()){
                if(r - l + 1 < len){
                    len = r - l + 1;
                    start = l;
                }

                char d = s[l];
                l++;
                //if the current left point to char in the need, 
                if(need.count(d)){
                    //if current num is equal, meaning we need to subtract qualified valid nums
                    if(window[d] == need[d]){
                        valid--;
                    }
                    window[d]--;
                }
            }
        }
        return (len == INT_MAX) ? "" : s.substr(start, len);
    }
};
