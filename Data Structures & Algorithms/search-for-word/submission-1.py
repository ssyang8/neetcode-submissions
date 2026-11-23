class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = '#'
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if dfs(nr, nc, k + 1):
                    return True
            board[i][j] = word[k]
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
