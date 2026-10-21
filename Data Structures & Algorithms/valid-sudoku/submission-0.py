class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set()] * 9
        cols = [set()] * 9
        grid = [set()] * 9
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c in rows[i]:
                    return False
                if c in cols[j]:
                    return False
                if c in grid[i / 3 * 3 + j / 3]:
                    return False