class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        m, n = len(matrix), len(matrix[0])
        def dfs(i, j, pre):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= pre:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = 1 + max(dfs(i - 1, j, matrix[i][j]), dfs(i + 1, j, matrix[i][j]), dfs(i, j - 1, matrix[i][j]), dfs(i, j + 1, matrix[i][j]))
            return cache[(i, j)]
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
            
        return ans
            
            