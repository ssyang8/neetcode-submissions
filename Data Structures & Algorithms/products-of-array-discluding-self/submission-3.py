class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= product
            product *= nums[i]
        
        return prefix