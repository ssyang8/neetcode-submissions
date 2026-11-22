class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 数学剪枝：n 个节点的树必定恰好有 n - 1 条边
        if len(edges) != n - 1:
            return False

        # 1. 双向建图（你这一步已经改对了）
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. 只保留一个 visited 集合
        visited = set()

        # 3. 传入 prev 记录父节点，防止走回头路误判为环
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            
            for neighbor in adj[curr]:
                if neighbor == prev:  # 跳过刚走过来的父节点
                    continue
                if not dfs(neighbor, curr):
                    return False
            
            return True

        # 4. 只从 0 出发跑一次：既要无环，也要所有 n 个节点全部连通
        return dfs(0, -1) and len(visited) == n
