class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;
        while(l < r){
            //if left is alpha or num, ++l;
            if(!isalnum(s[l])){
                ++l;
            //if right is alpha or num, --r;
            }else if(!isalnum(s[r])){
                --r;
            //if tolower(s[l]) != tolower(s[r]), return false;
            }else if(tolower(s[l]) != tolower(s[r])) return false;
            else{
                ++l;
                --r;
            }
        }
        return true;
    }
};
