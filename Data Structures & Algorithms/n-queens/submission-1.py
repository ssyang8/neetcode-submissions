from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        # 三个集合分别记录已占用的：行、主对角线(i - j)、副对角线(i + j)
        rows = set()
        diag1 = set()  # i - j
        diag2 = set()  # i + j
        
        def backtrack(j: int):
            # 终止条件：所有列都放完了
            if j == n:
                res.append(["".join(row) for row in board])
                return
            
            # 尝试当前列 j 的每一行 i
            for i in range(n):
                # O(1) 冲突判断
                if i in rows or (i - j) in diag1 or (i + j) in diag2:
                    continue
                
                # 1. 做选择（放置皇后并记录占用）
                board[i][j] = 'Q'
                rows.add(i)
                diag1.add(i - j)
                diag2.add(i + j)
                
                # 2. 递归进入下一列
                backtrack(j + 1)
                
                # 3. 撤销选择（回溯清理）
                board[i][j] = '.'
                rows.remove(i)
                diag1.remove(i - j)
                diag2.remove(i + j)
                
        backtrack(0)
        return res
