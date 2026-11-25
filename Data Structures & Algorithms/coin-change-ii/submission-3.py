class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}

        def dfs(i: int, rem: int) -> int:
            if (i, rem) in cache:
                return cache[(i, rem)]
            if rem == 0:
                return 1
            if rem < 0:
                return 0

            ans = 0
            # 从 i 开始往后枚举，不回头（去重）；下一层传 j 允许重复使用当前硬币
            for j in range(i, n):
                ans += dfs(j, rem - coins[j])

            cache[(i, rem)] = ans
            return ans

        return dfs(0, amount)
