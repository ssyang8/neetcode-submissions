class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        len1, len2 = len(word1), len(word2)

        def dfs(i: int, j: int) -> int:
            # 1. 刹车片：一方耗尽时，剩下的全部靠删除或插入补齐
            if i == len1:
                return len2 - j
            if j == len2:
                return len1 - i
            if (i, j) in cache:
                return cache[(i, j)]

            # 2. 甩手掌柜
            if word1[i] == word2[j]:
                # 字符相同：无需操作，直接双双后移
                ans = dfs(i + 1, j + 1)
            else:
                # 字符不同：删除 word1[i] / 插入 word2[j] / 替换 word1[i]，三者全都是 1 步
                ans = 1 + min(
                    dfs(i + 1, j),      # 删除
                    dfs(i, j + 1),      # 插入
                    dfs(i + 1, j + 1)   # 替换
                )

            cache[(i, j)] = ans
            return ans

        return dfs(0, 0)