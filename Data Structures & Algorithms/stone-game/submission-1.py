class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        n = len(piles)
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i > j:
                return 0
            ans = max(
                piles[i] - dfs(i + 1, j),
                piles[j] - dfs(i, j - 1)
            )
            cache[(i, j)] = ans
            return ans

        # 只要 Alice 最终净胜分 > 0，就赢了
        return dfs(0, n - 1) > 0

            
