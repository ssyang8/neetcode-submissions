class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}  # 记录 (i, j) -> bool，避免重复判断同一个区间
        res = s[0]

        def dfs(i: int, j: int) -> bool:
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]

            # 首尾相等，且去掉首尾后的内部子串也是回文
            memo[(i, j)] = (s[i] == s[j]) and dfs(i + 1, j - 1)
            return memo[(i, j)]

        # 枚举所有可能的左右端点 (i, j)
        for i in range(n):
            for j in range(i, n):
                if j - i + 1 > len(res) and dfs(i, j):
                    res = s[i : j + 1]

        return res
