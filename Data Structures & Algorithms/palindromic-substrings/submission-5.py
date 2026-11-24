class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 表示子串 s[i..j] 是否为回文串
        dp = [[False] * n for _ in range(n)]
        res = 0

        # i 从下往上倒着遍历，j 从 i 往右正着遍历
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    # 长度 <= 3（即 j - i <= 2：单个字符 "a"、两个字符 "aa"、三个字符 "aba"）
                    # 只要首尾相等就必然是回文；否则查左下角 dp[i + 1][j - 1]
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1

        return res
