class Solution {
public:
    int maxArea(vector<int>& heights) 
    {
        int left = 0;
        int right = heights.size() - 1;
        int ans = INT_MIN;
        while(left<right)
        {
            int size = (right - left) * min(heights[left], heights[right]);
            ans = max(ans, size);
            if(heights[left] <= heights[right]) left++;
            else right--;
        }
        return ans;
        
    }
};
