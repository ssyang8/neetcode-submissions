class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        m, n = len(text1), len(text2)
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= m or j >= n:
                return 0
            match = text1[i] == text2[j]
            ans = 0
            if match:
                ans = 1 + dfs(i + 1, j + 1)
            else:
                ans = max(dfs(i + 1, j), dfs(i, j + 1))
            cache[(i, j)] = ans
            return cache[(i, j)]
        return dfs(0, 0)