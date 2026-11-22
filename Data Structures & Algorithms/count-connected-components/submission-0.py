class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        component = n
        rank = [1 for _ in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def unionByRank(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            
            if rank[pu] <= rank[pv]:
                parent[pu] = pv
                rank[pv] += rank[pu]
            else:
                parent[pv] = pu
                rank[pu] += rank[pv]
            return True
        for u, v in edges:
            if unionByRank(u, v):
                component -= 1
        
        return component
                
