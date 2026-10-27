class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            return area
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea

        