class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        n = len(stones)
        cache = {}
        def dfs(i, rem):
            if (i, rem) in cache:
                return cache[(i, rem)]
            if rem < 0:
                return float("-inf")
            if i >= n:
                return 0
            ans = 0
            for j in range(i, n):
                ans = max(ans, stones[j] + dfs(j + 1, rem - stones[j]))
            cache[(i, rem)] = ans
            return cache[(i, rem)]
        res = sum(stones) - 2 * dfs(0, target)
        return res
            

            