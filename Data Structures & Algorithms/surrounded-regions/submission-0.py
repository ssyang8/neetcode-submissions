class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if (
                r < 0 or r >= m or c < 0 or c >= n
                or board[r][c] != 'O'
            ):
                return

            board[r][c] = 'Q'
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)

        # 从上下边界出发
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Q':
                    board[i][j] = 'O'
        

