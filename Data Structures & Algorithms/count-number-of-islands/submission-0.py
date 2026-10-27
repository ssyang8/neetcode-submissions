class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(x,y):
            q = deque([(x,y)])
            while q:
                sz = len(q)
                for _ in range(sz):
                    curX, curY = q.popleft()
                    for dx, dy in d:
                        nx, ny = curX+dx, curY+dy
                        if nx<0 or nx>=m or ny<0 or ny>=n or grid[nx][ny]=='0':
                            continue
                        grid[nx][ny]='0'
                        q.append((nx,ny))

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    bfs(i,j)
                    res+=1
        return res