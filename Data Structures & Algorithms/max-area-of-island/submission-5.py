class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] <= self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        return True
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def getPos(r, c):
            return r * n + c
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dsu = DSU(m * n)
        area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dr, dc in directions:
                        nr, nc = i + dr, j + dc
                        if (nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 1):
                            continue
                        dsu.unionBySize(getPos(i, j), getPos(nr, nc))
                    root = dsu.find(getPos(i, j))
                    area = max(area, dsu.size[root])
        return area







