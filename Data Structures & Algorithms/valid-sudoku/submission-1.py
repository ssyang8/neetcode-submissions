class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c == ".":
                    continue
                if c in rows[i]:
                    return False
                if c in cols[j]:
                    return False
                if c in grid[i // 3 * 3 + j // 3]:
                    return False
                rows[i].add(c)
                cols[j].add(c)
                grid[i // 3 * 3 + j // 3].add(c)
        return True