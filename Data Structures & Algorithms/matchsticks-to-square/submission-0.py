class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)  # 从大到小排序，大幅加速剪枝
        if matchsticks[0] > target:
            return False

        n = len(matchsticks)
        used = [False] * n

        def dfs(start: int, j: int, curr_sum: int) -> bool:
            # 1. 凑满 3 条边，剩下的火柴必然刚好凑成第 4 条边
            if j == 3:
                return True

            # 2. 当前桶凑满了，从头（start = 0）开始装第 j + 1 个桶
            if curr_sum == target:
                return dfs(0, j + 1, 0)

            for i in range(start, n):
                if used[i] or curr_sum + matchsticks[i] > target:
                    continue
                # 同层去重剪枝：同样长度的火柴刚试过且失败了，直接跳过
                if i > 0 and matchsticks[i] == matchsticks[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                if dfs(i + 1, j, curr_sum + matchsticks[i]):
                    return True
                used[i] = False

                # 核心大剪枝：如果当前桶是空的（curr_sum == 0），放第一根火柴就失败了，
                # 说明这根火柴放进任何空桶都会失败，直接返回 False！
                if curr_sum == 0:
                    return False

            return False

        return dfs(0, 0, 0)
