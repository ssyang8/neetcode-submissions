class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []
        path = []
        def dfs(i):
            if len(path) == n:
                res.append(path[:])
            if i >= n:
                return
            
            for j in range(n):
                if used[j]:
                    continue
                path.append(nums[j])
                used[j] = True
                dfs(i + 1)
                path.pop()
                used[j] = False
        dfs(0)
        return res
