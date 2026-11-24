class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == 1:
                return 1
            if i == 0 or i < 0:
                return float("-inf")
            ans = float("-inf")
            for j in range(1, i):
                ans = max(ans, j * dfs(i - j), j * (i - j))
            cache[(i)] = ans
            return ans
        return dfs(n)
