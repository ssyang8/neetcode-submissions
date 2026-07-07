class Solution {
public:
    int findMin(vector<int> &nums) {
        int left = 0;
        int right = nums.size() - 1;
        int res = nums[0];
        while(left <= right){
            //if current left < right, means current interval is ordered, so we can update the res by left
            if(nums[left] <  nums[right]){
                res = min(nums[left], res);
                break;
            }
            int mid = left + (right - left) / 2;
            res = min(res, nums[mid]);
            //if left < right, but left < mid, means the left part of rotated array is biggerm try to find the res in right
            if(nums[left] <=  nums[mid]){

                left = mid + 1;
            
            } 
            else{
                right = mid - 1;
            }

        }
        return res;
    }
};
