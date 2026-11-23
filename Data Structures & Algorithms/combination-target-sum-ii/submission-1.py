class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        used = [False] * n
        def dfs(start, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, n):
                if i >= 1 and candidates[i] == candidates[i - 1] and used[i - 1] == False:
                    continue
                used[i] = True
                path.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                path.pop()
                used[i] = False
        candidates.sort()
        dfs(0, 0)
        return res