class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        rows = set()
        diag1 = set()  # i - j
        diag2 = set()  # i + j
        
        def backtrack(j: int):
            nonlocal count
            # 终止条件：所有列都放完了，方案数 +1
            if j == n:
                count += 1
                return
            
            for i in range(n):
                if i in rows or (i - j) in diag1 or (i + j) in diag2:
                    continue
                
                # 做选择（只记录占用，连棋盘都不用画）
                rows.add(i)
                diag1.add(i - j)
                diag2.add(i + j)
                
                backtrack(j + 1)
                
                # 撤销选择
                rows.remove(i)
                diag1.remove(i - j)
                diag2.remove(i + j)
                
        backtrack(0)
        return count
