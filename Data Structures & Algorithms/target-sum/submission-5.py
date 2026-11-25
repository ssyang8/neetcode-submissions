class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}
        def dfs(i, cur_sum):
            if (i, cur_sum) in cache:
                return cache[(i, cur_sum)]
            if cur_sum == target and i >= n:
                return 1
            if i >= n:
                return 0
            cache[(i, cur_sum)] = dfs(i + 1, cur_sum - nums[i]) + dfs(i + 1, cur_sum + nums[i])
            return cache[(i, cur_sum)]
        
        return dfs(0, 0)
            