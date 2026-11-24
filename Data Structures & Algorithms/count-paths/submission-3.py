class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            ans = dfs(i - 1, j) + dfs(i, j - 1)
            cache[(i, j)] = ans
            return cache[(i, j)]
        return dfs(m - 1, n - 1)