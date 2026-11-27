class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def dfs(left, right):
            if left + 1 >= right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            
            ans = 0
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]
                ans = max(ans, dfs(left, i) + coins + dfs(i, right))
            cache[(left, right)] = ans
            return ans
        return dfs(0, len(nums) - 1)