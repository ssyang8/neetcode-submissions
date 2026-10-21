class Solution {
public:
    bool checkValidString(string s) {
        int left = 0;
        int right = 0;
        int wild = 0;
        for(auto& c : s){
            if(c == '(') left++;
            else if(c == ')') right++;
            else wild++;

        }
        if(left + wild - right <= 0 || right + wild - left <=0) return false;
        return true;
    }
};
