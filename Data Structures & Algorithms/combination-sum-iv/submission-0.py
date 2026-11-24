class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        n = len(nums)
        def dfs(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in cache:
                return cache[i]
            
            ans = 0
            for j in range(n):
                ans += dfs(i - nums[j])
            cache[i] = ans
            return ans
        return dfs(target)
        