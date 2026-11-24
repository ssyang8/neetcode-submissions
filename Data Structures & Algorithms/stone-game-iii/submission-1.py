class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        cache = {}
        def dfs(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            ans = float("-inf")
            take = 0
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    # 我拿到的分 - 对手在剩余局面的净胜分
                    ans = max(ans, take - dfs(i + k + 1))
            cache[i] = ans
            return cache[i]
        diff = dfs(0)
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"

