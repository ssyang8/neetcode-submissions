class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for rem in range(1, n + 1):
            for j in range(1, int(rem ** 0.5) + 1):
                dp[rem] = min(dp[rem], 1 + dp[rem - j * j])

        return dp[n]
