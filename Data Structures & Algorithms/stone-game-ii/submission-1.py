class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # 1. 预处理后缀和：suffix[i] 表示从第 i 堆到最后一堆的总石头数
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        cache = {}

        def dfs(i: int, M: int) -> int:
            if (i, M) in cache:
                return cache[(i, M)]
            if i >= n:
                return 0
            # 剪枝优化：如果剩下的堆数 <= 2M，当前玩家直接全包圆
            if i + 2 * M >= n:
                return suffix[i]

            ans = 0
            # j 代表这一轮拿走几堆（范围 1 到 2M，且不能超过剩余堆数 n - i）
            for j in range(1, min(2 * M, n - i) + 1):
                # 剩余总石头 suffix[i] 减去对手下一轮能拿走的最大值 = 自己最终拿到的总数
                ans = max(ans, suffix[i] - dfs(i + j, max(j, M)))

            cache[(i, M)] = ans
            return ans

        return dfs(0, 1)
