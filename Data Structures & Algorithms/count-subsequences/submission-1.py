class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        cache = {}
        def dfs(i, j):
            if j == len_t:
                return 1
            if i >= len_s:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            ans = 0 # 2. 甩手掌柜：
            # 分支 A（永远可选）：跳过 s[i]，留着 s 后面去匹配 t[j]
            ans = dfs(i + 1, j)

            # 分支 B（仅当字符相等时额外可选）：用 s[i] 匹配掉 t[j]
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)

            cache[(i, j)] = ans
            return ans
        return dfs(0, 0)
            
        