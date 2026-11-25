class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}
        def dfs(i, can_buy):
            if i >= n:
                return 0
            if (i, can_buy) in cache:
                return cache[(i, can_buy)]
            if can_buy:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)
                ans = max(buy, skip)
            else:
                sell = prices[i] + dfs(i + 2, True)  # 卖出直接跳过冷冻期
                hold = dfs(i + 1, False)
                ans = max(sell, hold)
            cache[(i, can_buy)] = ans
            return ans
        return dfs(0, True)