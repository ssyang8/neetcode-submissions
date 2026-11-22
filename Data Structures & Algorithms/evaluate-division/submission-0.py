from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. 双向建带权图（你这一步完全写对了）
        adj = defaultdict(list)
        for (a, b), val in zip(equations, values):
            adj[a].append((b, val))
            adj[b].append((a, 1.0 / val))

        def dfs(cur: str, target: str, acc: float, visited: set) -> float:
            # 节点不在图中，直接无解
            if cur not in adj or target not in adj:
                return -1.0
            if cur == target:
                return acc

            # 进入当前节点立刻标记已访问（防止绕圈死循环，且走不通的死胡同无需取消标记）
            visited.add(cur)

            for nxt, weight in adj[cur]:
                if nxt not in visited:
                    # 乘法直接写在参数里，不污染当前层的 acc
                    ans = dfs(nxt, target, acc * weight, visited)
                    # 只有真正找到了路径，才把结果层层往上返回
                    if ans != -1.0:
                        return ans

            # 所有邻居都是死胡同，返回 -1.0
            return -1.0

        # 每次 query 传入一个全新的 visited 集合
        return [dfs(a, b, 1.0, set()) for a, b in queries]
