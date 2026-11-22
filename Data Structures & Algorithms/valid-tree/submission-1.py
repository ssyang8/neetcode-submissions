class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            
            for neighbor in adj[curr]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, curr):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
