from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # 节点编号从 1 到 n，所以开 n + 1 长度
        parent = list(range(n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  # 路径压缩
            return parent[x]

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            # 两个节点已经在同一个集合里，说明再连这条边就会成环
            if root_u == root_v:
                return [u, v]
            # 否则合并两个集合
            parent[root_u] = root_v

        return []
