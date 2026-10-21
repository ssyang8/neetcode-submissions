class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == val:
                while l <= r:
                    if nums[r] == val:
                        r -= 1
                    else:
                        nums[l] = nums[r]
                        nums[r] = val
                        break
            l += 1
        
        return r + 1