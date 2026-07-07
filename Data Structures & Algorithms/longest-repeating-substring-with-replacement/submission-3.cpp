class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> mp;
        int l = 0;
        int count = 0;
        int res = 0;
        //count meaning the biggest in the process of making the window larger,
        //some element in the window has reach this frequence
        //our window will always keep the largest size, since some combination has reached this
        //even if the element of current window can not make it, it does not interfere with the final answer
        //we try to include r, to see, through include r, if we can use this new element to form a bigger window
        for(int r = 0; r < s.size(); ++r){
            mp[s[r]]++;
            count = max(count, mp[s[r]]);
            //as long as the window - most frequent element excess k meaning we cannot make the window larger
            if(r - l + 1 - count > k){

                mp[s[l]]--;
                l++;
            }
            res = max(res, r - l + 1);

        }
        return res;
    }
};
