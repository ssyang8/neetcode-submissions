class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numOranges = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numOranges += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        res = 0
        oranges = 0
        while q:
            sz = len(q)
            isInfect = False
            for _ in range(sz):
                r, c = q.popleft() 
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        isInfect = True
                        grid[nr][nc] = 2
                        oranges += 1
                        q.append((nr, nc))
            if isInfect:
                res += 1
        return res if oranges == numOranges else -1

        