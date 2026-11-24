class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if i in cache:
                return cache[i]
            ans = float('inf')
            for c in coins:
                ans = min(ans, 1 + dfs(i - c))
            cache[i] = ans
            return ans
        res = dfs(amount)
        return res if res != float('inf') else -1
