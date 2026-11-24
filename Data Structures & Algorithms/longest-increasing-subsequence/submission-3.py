class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)
        def dfs(i):
            if i == n:
                return 0
            if i in cache:
                return cache[i]
            ans = 1
            for j in range(i, n):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))
            cache[i] = ans
            return cache[i]
        return max(dfs(i) for i in range(n))