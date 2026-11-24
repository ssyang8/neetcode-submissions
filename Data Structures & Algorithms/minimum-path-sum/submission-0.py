class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i < 0 or j < 0:
                return float("inf")
            if i == 0 and j == 0:
                return grid[0][0]
            cur = grid[i][j]
            ans = min(cur + dfs(i - 1, j), cur + dfs(i, j - 1))
            cache[(i, j)] = ans
            return ans
        return dfs(m - 1, n - 1)
