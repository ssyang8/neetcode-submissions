class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        # 1. 长度对不上，直接淘汰
        if len1 + len2 != len3:
            return False

        cache = {}

        def dfs(i: int, j: int) -> bool:
            # 2. 刹车片：两个字符串都刚好匹配到末尾
            if i == len1 and j == len2:
                return True
            if (i, j) in cache:
                return cache[(i, j)]

            # 3. 甩手掌柜：只要 s1 或 s2 有一边能走通就行
            ans = False
            # 宇宙 A：s1 还没用完，且当前字符刚好等于 s3[i + j]
            if i < len1 and s1[i] == s3[i + j]:
                ans = ans or dfs(i + 1, j)

            # 宇宙 B：s2 还没用完，且当前字符刚好等于 s3[i + j]
            if j < len2 and s2[j] == s3[i + j]:
                ans = ans or dfs(i, j + 1)

            cache[(i, j)] = ans
            return ans

        return dfs(0, 0)
